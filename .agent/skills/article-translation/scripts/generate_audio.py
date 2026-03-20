#!/usr/bin/env python3
"""
Audio Generation Script for Article Translation
Uses edge-tts to generate English and Japanese audio from translated markdown files.

Usage:
    .venv-audio/bin/python .agent/skills/article-translation/scripts/generate_audio.py translations/YYYY-MM-DD/
    .venv-audio/bin/python .agent/skills/article-translation/scripts/generate_audio.py translations/YYYY-MM-DD/{slug}-en.md
"""

import re
import sys
import asyncio
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Error: edge-tts not installed.")
    print("Setup: python -m venv .venv-audio && .venv-audio/bin/pip install edge-tts")
    sys.exit(1)


# Voice configurations for article narration (single narrator per language)
VOICES = {
    "en": "en-US-JennyNeural",   # Warm, natural, neutral American English
    "ja": "ja-JP-NanamiNeural",  # Clear, polished standard Japanese
}


def detect_language(filepath: Path) -> str:
    """
    Detect target language from filename suffix.
    e.g.  article-en.md  → 'en'
          article-ja.md  → 'ja'
    Returns 'en' or 'ja', or None if unknown.
    """
    stem = filepath.stem  # e.g. "climate-change-en"
    if stem.endswith("-en"):
        return "en"
    if stem.endswith("-ja"):
        return "ja"
    return None


def extract_full_text(markdown_content: str, language: str) -> str:
    """
    Extract the 'Full Text' section from a translation markdown file.

    For English files, looks for '## Full English Text'
    For Japanese files, looks for '## 全文（日本語）'

    Returns the extracted plain text (markdown formatting stripped).
    """
    if language == "en":
        # Match section header variants
        pattern = r"## Full English Text\s*\n(.*?)(?=\n##|\Z)"
    else:
        pattern = r"## 全文（日本語）\s*\n(.*?)(?=\n##|\Z)"

    match = re.search(pattern, markdown_content, re.DOTALL)
    if not match:
        # Fallback: try to extract all text from the comparison table (second column)
        return extract_text_from_table(markdown_content, language)

    raw = match.group(1).strip()
    # Strip markdown formatting: bold, italic, code, links
    raw = re.sub(r"\*\*(.+?)\*\*", r"\1", raw)
    raw = re.sub(r"\*(.+?)\*", r"\1", raw)
    raw = re.sub(r"`(.+?)`", r"\1", raw)
    raw = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", raw)
    # Remove blockquote markers
    raw = re.sub(r"^> ?", "", raw, flags=re.MULTILINE)
    # Collapse multiple blank lines
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def extract_text_from_table(markdown_content: str, language: str) -> str:
    """
    Fallback: extract translated text from the comparison table.
    Returns all translated sentences joined into paragraphs.
    """
    # Find the table section
    if language == "en":
        pattern = r"## Sentence-by-Sentence Comparison\s*\n(.*?)(?=\n##|\Z)"
    else:
        pattern = r"## 一文ずつの対照\s*\n(.*?)(?=\n##|\Z)"

    match = re.search(pattern, markdown_content, re.DOTALL)
    if not match:
        return ""

    section = match.group(1)
    lines = []

    for line in section.split("\n"):
        line = line.strip()
        if not line or line.startswith("|---") or line.startswith("| #"):
            continue
        if line.startswith("|"):
            # Table row: | # | Chinese | Translation |
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3:
                # Third column is the translation
                translation = parts[2]
                # Strip markdown bold/italic
                translation = re.sub(r"\*\*(.+?)\*\*", r"\1", translation)
                translation = re.sub(r"\*(.+?)\*", r"\1", translation)
                lines.append(translation)

    return " ".join(lines)


async def generate_audio(text: str, voice: str, output_file: Path):
    """
    Generate an MP3 audio file from text using the specified edge-tts voice.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)

    if not text:
        print(f"  ⚠ Skipping {output_file.name}: no text found")
        return

    print(f"  🎙 Voice: {voice}")
    print(f"  📝 Text length: {len(text)} characters")

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_file))
    print(f"  ✓ Saved: {output_file}")


async def process_file(md_file: Path):
    """
    Process a single translation markdown file and generate its audio counterpart.
    """
    if not md_file.exists():
        print(f"Error: File not found: {md_file}")
        return False

    language = detect_language(md_file)
    if language is None:
        print(f"  ⚠ Skipping {md_file.name}: cannot detect language (expected -en.md or -ja.md suffix)")
        return False

    print(f"\n📄 Processing: {md_file.name}")

    content = md_file.read_text(encoding="utf-8")
    text = extract_full_text(content, language)

    if not text:
        print(f"  ⚠ No translatable text found in {md_file.name}")
        return False

    # Output: same directory, same stem but with -audio suffix
    # e.g. climate-change-en.md → climate-change-en-audio.mp3
    audio_file = md_file.parent / f"{md_file.stem}-audio.mp3"
    voice = VOICES[language]

    await generate_audio(text, voice, audio_file)
    return True


async def process_directory(directory: Path):
    """
    Process all translation markdown files in a directory.
    Identifies files by their -en.md or -ja.md suffix.
    """
    if not directory.exists():
        print(f"Error: Directory not found: {directory}")
        return

    # Find translation files
    translation_files = [
        f for f in directory.glob("*.md")
        if f.name != "README.md"
        and not f.name.startswith(".")
        and (f.stem.endswith("-en") or f.stem.endswith("-ja"))
    ]

    if not translation_files:
        print(f"No translation files found in {directory}")
        print("Expected files ending in -en.md or -ja.md")
        return

    print(f"Found {len(translation_files)} translation file(s)")

    for md_file in sorted(translation_files):
        await process_file(md_file)

    print("\n✅ Audio generation complete!")


async def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generate_audio.py translations/YYYY-MM-DD/")
        print("  python generate_audio.py translations/YYYY-MM-DD/{slug}-en.md")
        sys.exit(1)

    target = Path(sys.argv[1])

    print("🎤 Article Translation — Audio Generator")
    print(f"Voices: EN={VOICES['en']}, JA={VOICES['ja']}\n")

    if target.is_file():
        await process_file(target)
    elif target.is_dir():
        await process_directory(target)
    else:
        print(f"Error: Path not found: {target}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
