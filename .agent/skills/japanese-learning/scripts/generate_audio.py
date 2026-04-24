#!/usr/bin/env python3
"""
Audio Generation Script for Japanese Vocabulary Learning
Uses edge-tts to generate word and sentence audio from markdown vocabulary files.

Usage:
    .venv-audio/bin/python .agent/skills/japanese-learning/scripts/generate_audio.py pages/other/japanese/YYYY-MM-DD_jaNNN.md
"""

import re
import os
import sys
import asyncio
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Error: edge-tts not installed. Install with:")
    print("  python -m venv .venv-audio")
    print("  .venv-audio/bin/pip install edge-tts")
    sys.exit(1)


# Japanese voice configuration
VOICE_JA = "ja-JP-NanamiNeural"  # Natural Japanese female voice


def extract_words(markdown_content):
    """
    Extract word readings (假名) from vocabulary markdown file.

    Returns:
        list: List of reading strings (e.g., ['こうこう', 'かん', ...])
    """
    words = []

    # Match table rows containing 假名 field
    # Format: | 假名 | こうこう [🔊](...) |
    pattern = r'\|\s*假名\s*\|\s*(.+?)\s*(?:\[🔊\])?\s*\|'
    matches = re.findall(pattern, markdown_content)

    for match in matches:
        # Clean up the reading — remove audio links and whitespace
        reading = re.sub(r'\s*\[🔊\]\(.*?\)\s*', '', match).strip()
        if reading and reading != '内容':
            words.append(reading)

    return words


def extract_sentences(markdown_content):
    """
    Extract example sentences (例句) from vocabulary markdown file.

    Returns:
        list: List of Japanese sentence strings
    """
    sentences = []

    # Match example sentence lines
    # Format: **例句**: 日本語の文... [🔊](...)
    pattern = r'\*\*例句\*\*\s*[:：]\s*(.+?)(?:\s*\[🔊\]|\s*$)'
    matches = re.findall(pattern, markdown_content, re.MULTILINE)

    for match in matches:
        # Clean up — remove audio links and furigana markers for TTS
        sentence = match.strip()
        # Remove markdown links
        sentence = re.sub(r'\[🔊\]\(.*?\)', '', sentence)
        # Keep furigana as-is — edge-tts handles Japanese text well
        sentence = sentence.strip()
        if sentence:
            sentences.append(sentence)

    return sentences


def extract_story(markdown_content):
    """
    Extract the short story (今日短文) Japanese text from vocabulary markdown file.

    Returns:
        str: The Japanese story text, or empty string if not found
    """
    # Find the 今日短文 section, then the 日本語 subsection
    pattern = r'## 📖 今日短文.*?### 日本語\s*\n(.*?)(?=\n### |\n## |$)'
    match = re.search(pattern, markdown_content, re.DOTALL)
    if not match:
        return ""

    story_text = match.group(1).strip()
    # Remove markdown formatting but keep the text
    # Remove audio links
    story_text = re.sub(r'\[🔊[^\]]*\]\([^)]*\)', '', story_text)
    # Remove bold markers
    story_text = re.sub(r'\*\*', '', story_text)
    # Remove image links
    story_text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', story_text)
    story_text = story_text.strip()
    return story_text


async def generate_audio_file(texts, output_file, voice=VOICE_JA, pause_ms=800):
    """
    Generate a single audio file from a list of text items using ffmpeg concat.

    Args:
        texts: List of text strings to convert to speech
        output_file: Output MP3 file path
        voice: edge-tts voice name
        pause_ms: Pause duration between items in milliseconds
    """
    import tempfile
    import subprocess

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not texts:
        print(f"  Warning: No text to generate for {output_file}")
        return False

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        segment_files = []

        # Generate a short silence file for pauses between words
        silence_file = temp_path / "silence.mp3"
        silence_result = subprocess.run([
            'ffmpeg', '-y', '-f', 'lavfi', '-i',
            f'anullsrc=r=24000:cl=mono',
            '-t', str(pause_ms / 1000.0),
            '-q:a', '9', '-acodec', 'libmp3lame',
            str(silence_file)
        ], capture_output=True, text=True)

        if silence_result.returncode != 0:
            print(f"  Warning: Could not generate silence file: {silence_result.stderr}")
            # Continue without silence — not critical

        for idx, text in enumerate(texts):
            print(f"  Generating segment {idx + 1}/{len(texts)}: {text[:30]}...")
            segment_file = temp_path / f"segment_{idx:03d}.mp3"

            try:
                communicate = edge_tts.Communicate(text, voice)
                await communicate.save(str(segment_file))
                segment_files.append(segment_file)

                # Add silence after each segment (except the last)
                if idx < len(texts) - 1 and silence_file.exists():
                    segment_files.append(silence_file)
            except Exception as e:
                print(f"  Error generating segment {idx}: {e}")
                continue

        if not segment_files:
            print(f"  Error: No audio segments generated for {output_file}")
            return False

        # Create concat file list for ffmpeg
        concat_file = temp_path / 'concat_list.txt'
        with open(concat_file, 'w') as f:
            for seg_file in segment_files:
                f.write(f"file '{seg_file.absolute()}'\n")

        # Use ffmpeg to concatenate all segments
        result = subprocess.run([
            'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
            '-i', str(concat_file),
            '-c', 'copy', str(output_path)
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"  Error combining audio: {result.stderr}")
            return False

        file_size = output_path.stat().st_size / 1024
        print(f"  ✓ Generated: {output_file} ({file_size:.0f} KB)")
        return True


async def process_vocabulary_file(vocab_file):
    """
    Process a vocabulary markdown file and generate word + sentence audio.

    Args:
        vocab_file: Path to vocabulary markdown file
    """
    vocab_path = Path(vocab_file)

    if not vocab_path.exists():
        print(f"Error: File not found: {vocab_file}")
        return False

    with open(vocab_path, 'r', encoding='utf-8') as f:
        content = f.read()

    base_name = vocab_path.stem
    output_dir = vocab_path.parent

    print(f"\n🎤 Processing: {vocab_path.name}")

    # Extract words, sentences, and story
    words = extract_words(content)
    sentences = extract_sentences(content)
    story = extract_story(content)

    print(f"  Found {len(words)} words, {len(sentences)} sentences, story: {'yes' if story else 'no'}")

    success = True

    # Generate word audio
    if words:
        word_output = output_dir / f"{base_name}-words.mp3"
        print(f"\n📝 Generating word audio ({len(words)} words)...")
        if not await generate_audio_file(words, word_output, pause_ms=1000):
            success = False
    else:
        print("  Warning: No words found to generate audio")

    # Generate sentence audio
    if sentences:
        sentence_output = output_dir / f"{base_name}-sentences.mp3"
        print(f"\n📝 Generating sentence audio ({len(sentences)} sentences)...")
        if not await generate_audio_file(sentences, sentence_output, pause_ms=1200):
            success = False
    else:
        print("  Warning: No sentences found to generate audio")

    # Generate story audio
    if story:
        story_output = output_dir / f"{base_name}-story.mp3"
        print(f"\n📖 Generating story audio...")
        if not await generate_audio_file([story], story_output, pause_ms=0):
            success = False
    else:
        print("  Warning: No story found to generate audio")

    if success:
        print(f"\n✅ Audio generation complete for {vocab_path.name}!")
    else:
        print(f"\n⚠️ Audio generation completed with some errors for {vocab_path.name}")

    return success


async def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python generate_audio.py <vocabulary_markdown_file>")
        print("\nExamples:")
        print("  python generate_audio.py pages/other/japanese/2026-04-25_ja001.md")
        sys.exit(1)

    target = sys.argv[1]
    target_path = Path(target)

    print("🎤 Japanese Vocabulary Audio Generation")
    print(f"Voice: {VOICE_JA}\n")

    if target_path.is_file():
        await process_vocabulary_file(target_path)
    elif target_path.is_dir():
        # Process all markdown files in directory
        md_files = sorted([
            f for f in target_path.glob("*_ja*.md")
            if f.name != "index.md"
        ])
        if not md_files:
            print(f"No vocabulary files found in {target}")
            sys.exit(1)
        print(f"Found {len(md_files)} vocabulary file(s)")
        for md_file in md_files:
            await process_vocabulary_file(md_file)
        print("\n✅ All audio generation complete!")
    else:
        print(f"Error: Invalid path: {target}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
