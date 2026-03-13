---
name: english-learning
description: Daily English learning skill that generates scenario-based dialogues in Chinese, English, and Japanese. Use when user says "开始今日任务" or wants to start their daily English practice. Supports IT and daily life scenarios with adjustable difficulty levels.
---

# English Learning Skill

This skill helps you practice English through daily scenario-based dialogues with multi-language support (Chinese, English, Japanese).

## When to use this skill

- User says "开始今日任务" or "start today's task" or "begin daily task"
- User says "start daily English practice" or "begin English learning"
- User wants to begin their daily English practice
- User wants to create a new learning session

## Workflow

### 1. Initialize Daily Task

When the user requests to start their daily task:

1. **Output location**: All dialogue files are created directly in `pages/other/english/` (the GitHub Pages site directory)
2. **Naming convention**: Use `YYYY-MM-DD_english{NN}.md` where NN is a 2-digit sequence (01, 02, 03) for the 3 dialogues of the day
   - Example: `2026-03-11_english01.md`, `2026-03-11_english02.md`, `2026-03-11_english03.md`
3. **Check if files exist**: If files with today's date already exist, ask user if they want to:
   - Continue with existing session
   - Overwrite the existing files

### 2. Load Configuration and History

1. **Read config**: Load `config.yaml` to get:
   - Available IT scenarios
   - Available daily life scenarios
   - Current difficulty level
2. **Read history**: Load `data/history.json` to check recently used scenarios

### 3. Present Scenarios for User Selection

Present all available scenarios to the user and let them choose 3 for today's session:

**Step 1: Load and Display Available Scenarios**

1. Read `config.yaml` to get all IT and daily life scenarios
2. Check `history.json` to show usage statistics (optional, for user information)
3. Present scenarios in two categories:

**IT/Computer Scenarios:**
List all available IT scenarios with their Chinese names and descriptions:

- Code Review Discussion (代码审查讨论)
- Sprint Planning Meeting (敏捷冲刺规划会议)
- Debugging Session (调试会话)
- [... all IT scenarios from config.yaml]

**Daily Life Scenarios:**
List all available daily life scenarios with their Chinese names and descriptions:

- Restaurant Ordering (餐厅点餐)
- Coffee Shop Chat (咖啡店闲聊)
- Weekend Plans (周末计划)
- [... all daily life scenarios from config.yaml]

**Step 2: User Selection**
Ask the user to select exactly 3 scenarios for today:

- User can choose any 3 scenarios from either category
- User specifies the dialogue type for each scenario:
  - **Meeting** (会议) - Formal, professional context
  - **Casual** (日常沟通) - Informal, relaxed conversation

**Example User Input:**

```
1. Code Review Discussion - Meeting
2. Debugging Session - Casual  
3. Coffee Shop Chat - Casual
```

**Step 3: Confirm Selection**
Show the user's selection and ask for confirmation before generating dialogues.

### 4. Generate Three Dialogues

Generate 3 natural, native-speaker dialogues with the following guidelines:

**Content Guidelines - Authenticity is Critical:**

⚠️ **AVOID "ESL Textbook English"** - The dialogue must sound like real native speakers, not language learning materials.

**Core Principles:**

1. **High Information Density**: Assume shared context - people working together don't explain everything
2. **Incomplete Sentences**: Real people use fragments, especially in responses ("The S3 stuff?", "Quick fix or migration?")
3. **Action Verbs Over Formal Phrases**: Use dynamic verb phrases instead of bureaucratic language
4. **Industry Jargon**: Use actual terminology that professionals use, not textbook definitions

**For IT/Tech Meetings:**

- ❌ AVOID: "This violates the principle of least privilege"
- ✅ USE: "Those perms are way too loose" / "We need to scope those down"
- ❌ AVOID: "Ensure we're using CloudFront for content delivery"
- ✅ USE: "Stick CloudFront in front" / "Put CloudFront in front of them"
- ❌ AVOID: "Will this have a significant impact on our AWS bill?"
- ✅ USE: "Is that gonna blow up the bill?" / "What's the hit on the budget?"
- ❌ AVOID: "Settings that aren't properly configured"
- ✅ USE: "Those buckets are public" / "We never locked them down"
- ❌ AVOID: "We created them for rapid prototyping"
- ✅ USE: "We used Admin access to move fast" / "We did that to unblock the prototype phase"

**Common Tech Meeting Patterns:**

- Use shorthand: "The S3 findings?", "Is this about the open buckets?"
- Use action verbs: "flip on", "kill", "patch", "scope down", "lock down", "ping [person/team]"
- Abbreviate naturally: "perms" (permissions), "prod" (production), "sync" (meeting/synchronize)
- Direct questions: "Quick fix or migration?", "What else?"
- Acknowledge with minimal words: "Got it", "Fair enough", "Cool", "Awesome"

**For Casual Conversations:**

- Use natural contractions: "I've been", "What's", "That's", "You're"
- Incomplete sentences are normal: "Pretty great!", "Really?", "Oh yeah?"
- Phrasal verbs everywhere: "get into", "figure out", "mess around with", "give it a shot"
- Drop subjects when obvious: "Sounds good" not "That sounds good"
- Use filler words naturally: "you know", "I mean", "like"

**For Daily Life Scenarios:**

- Casual responses: "Totally", "For sure", "Couldn't agree more"
- Soften suggestions: "Maybe we could...", "Want to...?", "How about...?"
- Show enthusiasm: "That's so cool!", "Awesome!", "I love that idea!"

**Difficulty Level Adaptation:**

- **初级 (Elementary)**: Still authentic but simpler structures, common vocabulary, clear (but not overly formal) communication
- **中级 (Intermediate)**: Mix of straightforward and idiomatic expressions, natural shortcuts, some technical jargon
- **高级 (Advanced)**: Full native-level communication with industry slang, cultural references, implicit understanding

**Dialogue Structure:**

- 2-4 speakers (depending on context)
- 10-15 exchanges total
- Natural conversation flow with realistic interruptions, agreements, clarifications

**Naming Convention:**

- Dialogue 1: `YYYY-MM-DD_english01.md`
- Dialogue 2: `YYYY-MM-DD_english02.md`
- Dialogue 3: `YYYY-MM-DD_english03.md`

All files are placed in: `pages/other/english/`

### 5. Generate Multi-language Content

For each dialogue, create a markdown file in `pages/other/english/` with the following structure:

**IMPORTANT — Jekyll Front-matter**:

Every generated `.md` file MUST begin with Jekyll front-matter so the page renders correctly on the GitHub Pages site:

```yaml
---
layout: default
title: "YYYY-MM-DD Scenario Name"
---
```

Example: `title: "2026-03-11 Tech Support Call"`

**File Template:**

```markdown
---
layout: default
title: "YYYY-MM-DD Scenario Name"
---

# English

{Scenario Name}  [EN 🔊](./{filename}-en.mp3)  [JA 🔊](./{filename}-ja.mp3)

## English Dialogue / 英文对话

| English | 中文 |
|---------|------|
| **[Speaker]**: [English dialogue line] | **[讲话者]**: [中文翻译] |
| **[Speaker]**: [English dialogue line] | **[讲话者]**: [中文翻译] |
| ... | ... |

### Grammar Explanations

[Explain key grammar structures used, numbered by occurrence]

1. **Structure**: [Grammar point]
   - **Example from dialogue**: [Quote from dialogue]
   - **Explanation**: [Simple explanation in Chinese and English]

### Vocabulary

[List key vocabulary with definitions and CEFR levels]

| English | Chinese | CEFR Level | Example from Dialogue |
|---------|---------|------------|----------------------|
| [word]  | [定义]   | [A1-C2]    | [例句]                |

---

## Japanese Dialogue / 日语对话

| 日本語 | 中文 |
|--------|------|
| **[Speaker]**: [Japanese dialogue line] | **[讲话者]**: [中文翻译] |
| **[Speaker]**: [Japanese dialogue line] | **[讲话者]**: [中文翻译] |
| ... | ... |

### 文法説明 (Grammar Explanations)

[Explain key grammar structures used]

1. **文法**: [Grammar point in Japanese]
   - **例**: [Quote from dialogue]
   - **説明**: [Explanation in Japanese and Chinese]

### 語彙 (Vocabulary)

[List key vocabulary with definitions and CEFR levels]

| 日本語 | 假名 | 中文 | CEFR Level | 例文 |
|--------|------|------|------------|------|
| [word] | [kana] | [定义] | [A1-C2]    | [例句] |

---

[← back to English](./) | [← back to Other](..) | [← back to home](/)
```

**Key Points:**
- The `{filename}` in the audio links is the current file's name without extension (e.g., `2026-03-11_english01`)
- Audio links appear right after the `# English` heading, on the same line as the scenario name
- The footer navigation links at the bottom are required for site consistency
- Side-by-side table format makes it easier to learn
- Tables render beautifully on GitHub Pages

### 5.5. Generate Audio Files (Optional but Recommended)

After generating the dialogue markdown files, create audio versions for pronunciation practice:

**Tool**: Use `edge-tts` for high-quality, multilingual text-to-speech

**Command**:

```bash
# Generate audio for a single dialogue file in pages/other/english/
.venv-audio/bin/python .agent/skills/english-learning/scripts/generate_audio.py pages/other/english/YYYY-MM-DD_english01.md

# Or generate audio for all dialogue files matching today's date
.venv-audio/bin/python .agent/skills/english-learning/scripts/generate_audio.py pages/other/english/YYYY-MM-DD_english01.md
.venv-audio/bin/python .agent/skills/english-learning/scripts/generate_audio.py pages/other/english/YYYY-MM-DD_english02.md
.venv-audio/bin/python .agent/skills/english-learning/scripts/generate_audio.py pages/other/english/YYYY-MM-DD_english03.md
```

**Output**: For each dialogue file, generates audio in `pages/other/english/`:

- `{filename}-en.mp3` - English audio (~500-700KB)
- `{filename}-ja.mp3` - Japanese audio (~500-700KB)

The `{filename}` is the exact name of the markdown file without `.md` (e.g., `2026-03-11_english01`).

**Features**:

- Automatically extracts dialogue text from English and Japanese sections
- Uses native voices (en-US-GuyNeural for English, ja-JP-NanamiNeural for Japanese)
- Includes speaker names in audio for clarity
- Works offline after initial setup

**Setup** (one-time):

```bash
# Create virtual environment for audio tools
python -m venv .venv-audio
.venv-audio/bin/pip install edge-tts
```

**Note**: Audio generation requires an internet connection for edge-tts to download voice models.

**IMPORTANT — Audio Links in Articles**:

After generating the audio files, ensure each dialogue `.md` file includes audio links in the header. The links should appear right after the `# English` heading:

```markdown
# English

{Scenario Name}  [EN 🔊](./{filename}-en.mp3)  [JA 🔊](./{filename}-ja.mp3)
```

This allows users to click and play the audio directly from the GitHub Pages article.

### 6. Archive Vocabulary

After generating dialogues, extract and archive vocabulary based on difficulty level:

**CEFR Filtering Rules:**

- **初级 (Elementary)**: Archive A1 and above (A1, A2, B1, B2, C1, C2) - all levels
- **中级 (Intermediate)**: Archive B1 and above (B1, B2, C1, C2) - intermediate to advanced
- **高级 (Advanced)**: Archive B2 to C2 (B2, C1, C2) - advanced levels only

**Archive Process:**

1. Extract vocabulary from all 3 generated dialogue files
2. Filter vocabulary based on current difficulty level and CEFR rules
3. Append filtered words to:
   - `vocabulary/english/README.md` for English words
   - `vocabulary/japanese/README.md` for Japanese words
4. Include metadata: word, definition, CEFR level, example, date, source scenario
5. Check for duplicates - skip words already in archive
6. Update timestamp in vocabulary files

**Important Notes:**

- Each word must be tagged with its CEFR level (A1, A2, B1, B2, C1, C2) during dialogue generation
- Only words matching the difficulty level criteria are archived
- Vocabulary files are cumulative and grow over time
- Duplicates are prevented by checking existing entries

### 7. Update History

After archiving vocabulary:

1. Update `data/history.json` with:
   - Date
   - Scenarios used
   - Dialogue types
   - Current difficulty level
2. Create an index entry in the dated directory with metadata

### 8. Session Summary (No Separate File Needed)

Since all dialogue articles are now placed in `pages/other/english/` with Jekyll front-matter, the `directory` layout index page (`pages/other/english/index.md`) automatically lists all articles under a `📑 Contents` section.

**No separate README.md or session summary file is needed.**

The `index.md` already exists and uses `layout: directory` which auto-generates the article list from all subpages with titles.

**IMPORTANT - Link Format**:

- **Use relative paths** for all markdown links within generated articles, NOT absolute `file:///` paths
- Audio files in same directory: Use `./{filename}-en.mp3` format
- Footer navigation: Use `[← back to English](./) | [← back to Other](..) | [← back to home](/)`
- **Never use** `file:///absolute/path` format in generated markdown files

## Important Notes

- **Natural language**: Focus on how native speakers actually talk, not textbook language
- **Avoid repetition**: Check history.json to avoid using the same scenarios too frequently
- **Appropriate difficulty**: Adjust complexity based on configured difficulty level
- **Cultural context**: Include culturally appropriate expressions and situations
- **Realistic scenarios**: Base dialogues on real workplace and life situations

## Configuration Management

Users can modify `config.yaml` to:

- Add new scenarios
- Change difficulty level
- Customize language settings

When generating content, always check the current configuration first.

## File Organization

```
# Skill files (unchanged)
.agent/skills/english-learning/
├── SKILL.md
├── config.yaml
├── data/
│   └── history.json
└── scripts/
    ├── init_daily_task.py
    ├── update_history.py
    ├── archive_vocabulary.py
    └── generate_audio.py

# Generated articles go here (GitHub Pages site)
pages/other/english/
├── index.md                            # Directory index (auto-lists articles)
├── YYYY-MM-DD_english01.md             # Session dialogue 1
├── YYYY-MM-DD_english02.md             # Session dialogue 2
├── YYYY-MM-DD_english03.md             # Session dialogue 3
├── {dialogue-1-slug}-en.mp3            # English audio for dialogue 1
├── {dialogue-1-slug}-ja.mp3            # Japanese audio for dialogue 1
├── {dialogue-2-slug}-en.mp3            # English audio for dialogue 2
├── {dialogue-2-slug}-ja.mp3            # Japanese audio for dialogue 2
├── {dialogue-3-slug}-en.mp3            # English audio for dialogue 3
└── {dialogue-3-slug}-ja.mp3            # Japanese audio for dialogue 3

# Vocabulary archives (unchanged)
vocabulary/
├── english/
│   └── README.md
└── japanese/
    └── README.md
```

## Error Handling

- If config.yaml is missing, use default scenarios
- If history.json is missing, create a new one
- If user selects same scenario as yesterday, warn but allow it
- If dialogue generation fails, provide a clear error message
