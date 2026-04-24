#!/usr/bin/env python3
"""
Audio Generation Script for Japanese Grammar Learning
Uses edge-tts to generate example and passage audio from grammar markdown files.

Usage:
    .venv-audio/bin/python .agent/skills/japanese-grammar/scripts/generate_audio.py pages/other/japanese-grammar/YYYY-MM-DD_grNNN.md
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


def strip_furigana(text):
    """
    Remove furigana annotations in full-width parentheses from Japanese text.
    e.g. 漢字（かんじ） → 漢字
    This prevents TTS from reading both the kanji and its reading aloud.
    """
    return re.sub(r'（[^）]*）', '', text)


def extract_examples(markdown_content):
    """
    Extract all example sentences from grammar markdown file.
    Matches both 原文例句 and AI補充例文 sections.

    Returns:
        list: List of Japanese sentence strings
    """
    sentences = []

    # Match lines that are numbered examples (1. 2. etc.) with Japanese text
    # Pattern: number + . or 、 + Japanese text + optional audio link
    # Examples appear after **原文例句:** and **AI補充例文:**
    lines = markdown_content.split('\n')

    in_example_section = False
    for line in lines:
        stripped = line.strip()

        # Detect example section headers
        if '**例句' in stripped or '**原文例句' in stripped or '**AI補充例文' in stripped:
            in_example_section = True
            continue

        # Exit example section on other headers or section breaks
        if stripped.startswith('**') and in_example_section and '例' not in stripped:
            in_example_section = False
            continue
        if stripped.startswith('##') or stripped.startswith('---'):
            in_example_section = False
            continue

        if in_example_section:
            # Match numbered example lines: 1. JP text [🔊]
            m = re.match(r'^\d+\.\s*(.+?)(?:\s*\[🔊\]|$)', stripped)
            if m:
                sentence = m.group(1).strip()
                # Remove audio markdown links
                sentence = re.sub(r'\[🔊\]\(.*?\)', '', sentence)
                # Remove furigana
                sentence = strip_furigana(sentence)
                sentence = sentence.strip()
                if sentence and not sentence.startswith('>'):
                    sentences.append(sentence)

    return sentences


def extract_passage(markdown_content):
    """
    Extract the short passage (今日短文) Japanese text from grammar markdown file.

    Returns:
        str: The Japanese passage text, or empty string if not found
    """
    # Find the 今日短文 section, then the 日本語 subsection
    pattern = r'## 📖 今日短文.*?### 日本語\s*\n(.*?)(?=\n### |\n## |$)'
    match = re.search(pattern, markdown_content, re.DOTALL)
    if not match:
        return ""

    passage_text = match.group(1).strip()
    # Remove markdown formatting but keep the text
    passage_text = re.sub(r'\[🔊[^\]]*\]\([^)]*\)', '', passage_text)
    passage_text = re.sub(r'\*\*', '', passage_text)
    passage_text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', passage_text)
    # Remove furigana
    passage_text = strip_furigana(passage_text)
    passage_text = passage_text.strip()
    return passage_text


async def generate_audio_file(texts, output_file, voice=VOICE_JA, pause_ms=800):
    """
    Generate a single audio file from a list of text items using ffmpeg concat.
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

        # Generate silence file for pauses
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

        for idx, text in enumerate(texts):
            print(f"  Generating segment {idx + 1}/{len(texts)}: {text[:40]}...")
            segment_file = temp_path / f"segment_{idx:03d}.mp3"

            try:
                communicate = edge_tts.Communicate(text, voice)
                await communicate.save(str(segment_file))
                segment_files.append(segment_file)

                if idx < len(texts) - 1 and silence_file.exists():
                    segment_files.append(silence_file)
            except Exception as e:
                print(f"  Error generating segment {idx}: {e}")
                continue

        if not segment_files:
            print(f"  Error: No audio segments generated for {output_file}")
            return False

        # Concat with ffmpeg
        concat_file = temp_path / 'concat_list.txt'
        with open(concat_file, 'w') as f:
            for seg_file in segment_files:
                f.write(f"file '{seg_file.absolute()}'\n")

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


async def process_grammar_file(grammar_file):
    """
    Process a grammar markdown file and generate example + passage audio.
    """
    grammar_path = Path(grammar_file)

    if not grammar_path.exists():
        print(f"Error: File not found: {grammar_file}")
        return False

    with open(grammar_path, 'r', encoding='utf-8') as f:
        content = f.read()

    base_name = grammar_path.stem
    output_dir = grammar_path.parent

    print(f"\n🎤 Processing: {grammar_path.name}")

    # Extract examples and passage
    examples = extract_examples(content)
    passage = extract_passage(content)

    print(f"  Found {len(examples)} example sentences, passage: {'yes' if passage else 'no'}")

    success = True

    # Generate example audio
    if examples:
        example_output = output_dir / f"{base_name}-examples.mp3"
        print(f"\n📝 Generating example audio ({len(examples)} sentences)...")
        if not await generate_audio_file(examples, example_output, pause_ms=1200):
            success = False
    else:
        print("  Warning: No examples found to generate audio")

    # Generate passage audio
    if passage:
        passage_output = output_dir / f"{base_name}-passage.mp3"
        print(f"\n📖 Generating passage audio...")
        if not await generate_audio_file([passage], passage_output, pause_ms=0):
            success = False
    else:
        print("  Warning: No passage found to generate audio")

    if success:
        print(f"\n✅ Audio generation complete for {grammar_path.name}!")
    else:
        print(f"\n⚠️ Audio generation completed with some errors for {grammar_path.name}")

    return success


async def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python generate_audio.py <grammar_markdown_file>")
        print("\nExamples:")
        print("  python generate_audio.py pages/other/japanese-grammar/2026-04-25_gr001.md")
        sys.exit(1)

    target = sys.argv[1]
    target_path = Path(target)

    print("🎤 Japanese Grammar Audio Generation")
    print(f"Voice: {VOICE_JA}\n")

    if target_path.is_file():
        await process_grammar_file(target_path)
    elif target_path.is_dir():
        md_files = sorted([
            f for f in target_path.glob("*_gr*.md")
            if f.name != "index.md"
        ])
        if not md_files:
            print(f"No grammar files found in {target}")
            sys.exit(1)
        print(f"Found {len(md_files)} grammar file(s)")
        for md_file in md_files:
            await process_grammar_file(md_file)
        print("\n✅ All audio generation complete!")
    else:
        print(f"Error: Invalid path: {target}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
