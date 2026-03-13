# Audio Generation Setup and Testing

## Installation Status

Installing edge-tts via pipx (in progress)...

## Quick Test Instructions

Once installation is complete, test audio generation:

### Option 1: Test with a single dialogue file

```bash
python .agent/skills/english-learning/scripts/generate_audio.py 2026-01-31/cloud-security-review-meeting.md
```

### Option 2: Process entire directory

```bash
python .agent/skills/english-learning/scripts/generate_audio.py 2026-01-31/
```

## Alternative: Direct Python Installation

If pipx installation takes too long, you can use pip in a virtual environment:

```bash
# Create virtual environment
cd /home/peigen/Dev/hardfork/english
python -m venv .venv

# Activate it
source .venv/bin/activate

# Install edge-tts
pip install edge-tts

# Run the script
python .agent/skills/english-learning/scripts/generate_audio.py 2026-01-31/
```

## Expected Output

After successful generation, you should see:

```
2026-01-31/
├── cloud-security-review-meeting.md
├── cloud-security-review-meeting-en.mp3  ✅
├── cloud-security-review-meeting-ja.mp3  ✅
├── technical-design-discussion-casual.md
├── technical-design-discussion-casual-en.mp3  ✅
├── technical-design-discussion-casual-ja.mp3  ✅
├── weekend-plans-casual.md
├── weekend-plans-casual-en.mp3  ✅
└── weekend-plans-casual-ja.mp3  ✅
```

## Voice Configuration

Current voices:

- English: `en-US-GuyNeural` (American Male)
- Japanese: `ja-JP-NanamiNeural` (Japanese Female)

To change voices, edit the `VOICES` dictionary in `generate_audio.py`.
