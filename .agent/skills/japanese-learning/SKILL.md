---
name: japanese-learning
description: Daily Japanese vocabulary learning skill that generates vocabulary cards from notes.csv with example sentences, mnemonics, and audio. Use when user says "开始今日任务" or wants to start their daily Japanese vocabulary practice. 1-year plan covering ~10,168 words.
---

# Japanese Vocabulary Learning Skill

This skill helps you learn Japanese vocabulary daily through structured vocabulary cards generated from a curated word list (10,168 words covering JLPT N5→N1).

## When to use this skill

- User says "开始今日任务" or "start today's task" or "begin daily task"
- User says "start daily Japanese vocabulary" or "開始日語學習"
- User wants to begin their daily Japanese vocabulary practice
- User wants to create a new vocabulary learning session

## Data Source

- **CSV File**: `.agent/skills/japanese-learning/data/notes.csv`
- **Total Words**: 10,168
- **Columns**: `level`, `word`, `pitch_accent`, `pos`, `reading`, `meaning`
- **Levels** (learning order):
  1. `1-N4+N5` — 1,568 words (基础)
  2. `2-N3::1-高频` — 454 words
  3. `2-N3::2-中低频` — 1,134 words
  4. `3-N2::1-高频` — 968 words
  5. `3-N2::2-中低频` — 1,963 words
  6. `4-N1::1-高频` — 1,191 words
  7. `4-N1::2-中频` — 1,199 words
  8. `4-N1::3-低频` — 1,692 words

## 1-Year Plan

- **Words per day**: Random between **28–35**
- **Order**: Original CSV order (no re-sorting within levels)
- **No review mechanism** — pure forward progress

| Phase | Duration | Level | Words |
|-------|----------|-------|-------|
| Phase 1 | ~2 months | N5+N4 | 1,568 |
| Phase 2 | ~2 months | N3 | 1,588 |
| Phase 3 | ~3.5 months | N2 | 2,931 |
| Phase 4 | ~5 months | N1 | 4,082 |

## Workflow

### 1. Check Progress

1. **Read progress**: Load `data/progress.yaml` from **this skill's directory** (`.agent/skills/japanese-learning/data/progress.yaml`)
2. Determine `current_line` — the next CSV line to read (1-indexed, line 1 = header)
3. If `current_line` > 10168, congratulate the user — all words completed!
4. **Check today's date**: If a file with today's date already exists in `pages/other/japanese/`, ask user if they want to overwrite or skip

### 2. Read Words from CSV

1. Open `.agent/skills/japanese-learning/data/notes.csv`
2. Generate a random number **N** between 28 and 35 (inclusive)
3. Read **N** rows starting from `current_line` (skip header row)
4. If fewer than N rows remain, read all remaining rows
5. Parse each row: `level`, `word`, `pitch_accent`, `pos`, `reading`, `meaning`

### 3. Generate Vocabulary Content

For each word, the AI must generate:

| Field | Source | Description |
|-------|--------|-------------|
| 単語 (Word) | CSV `word` | 日语原文 (汉字/片假名/平假名) |
| 重音 (Pitch Accent) | CSV `pitch_accent` | 音高标记 ⓪①②③ etc. |
| 假名 (Reading) | CSV `reading` | 平假名/片假名读音 |
| 词性 (Part of Speech) | CSV `pos` | 名、他動1、イ形 etc. |
| 意思 (Meaning) | CSV `meaning` | 中文释义 |
| JLPT Level | CSV `level` | N5-N1 分级 |
| 例句 (Example) | **AI Generated** | 日文例句 + 中文翻译 |
| 助记 (Mnemonic) | **AI Generated** | 记忆技巧 |

**Example Sentence Guidelines:**
- Must be natural, daily-use Japanese
- Difficulty should match the word's JLPT level
- **Do NOT include furigana** in parentheses like 漢字（かんじ） — the TTS audio will read both kanji and reading, causing double-reading. Write plain Japanese only: 漢字
- Provide Chinese translation
- Use the target word naturally in context

**Mnemonic Guidelines:**
- Use character decomposition (字源拆解) when applicable
- Use sound association (谐音联想) for katakana words
- Compare with Chinese characters when meanings differ
- Keep it short and memorable (1-2 sentences max)

### 4. Generate Markdown File

**Output location**: `pages/other/japanese/`
**Naming convention**: `YYYY-MM-DD_jaNNN.md` where NNN is the day number (001, 002, ...)

**IMPORTANT — Jekyll Front-matter**:

Every generated `.md` file MUST begin with Jekyll front-matter:

```yaml
---
layout: default
title: "Day NNN - JLPT XX 日语单词"
---
```

**File Template:**

```markdown
---
layout: default
title: "Day NNN - JLPT XX 日语单词"
---

# 📖 Day NNN — 日语单词学习

📅 YYYY-MM-DD | 📊 进度: XXX/10168 (X.X%) | 🎯 Level: JLPT XX

[🔊 单词朗读](./YYYY-MM-DD_jaNNN-words.mp3) | [🔊 例句朗读](./YYYY-MM-DD_jaNNN-sentences.mp3)

---

## 1. 高校

| 項目 | 内容 |
|------|------|
| 単語 | 高校 |
| 重音 | ⓪ |
| 假名 | こうこう [🔊](./YYYY-MM-DD_jaNNN-words.mp3) |
| 词性 | 名 |
| 意思 | 高中 |
| Level | N4+N5 |

**例句**: 私（わたし）は高校（こうこう）の時（とき）、サッカー部（ぶ）に入（はい）っていました。 [🔊](./YYYY-MM-DD_jaNNN-sentences.mp3)
> 我高中的时候加入了足球社。

**助记**: 高＝高等的，校＝学校 → 高等学校 = 高中。注意：日语的「高校」指高中，和中文的「高校」（大学）不同。

---

## 2. 間

| 項目 | 内容 |
|------|------|
| 単語 | 間 |
| 重音 | ① |
| 假名 | かん [🔊](./YYYY-MM-DD_jaNNN-words.mp3) |
| 词性 | 名 |
| 意思 | 间，期间 |
| Level | N4+N5 |

**例句**: この三年間（さんねんかん）、日本語（にほんご）を勉強（べんきょう）しています。 [🔊](./YYYY-MM-DD_jaNNN-sentences.mp3)
> 这三年来一直在学习日语。

**助记**: 「間」和中文"间"相同，表示时间或空间的间隔。日语中常作后缀用：三年間、時間。

---

## 3. ...

(continue for all N words)

---

## 📖 今日短文

以下短文包含了今天学习的所有单词，通过语境帮助你加深记忆。

[🔊 短文朗读](./YYYY-MM-DD_jaNNN-story.mp3)

### 日本語

（AI が今日の単語を全て使って書いた短い文章。自然な日本語で、ストーリー性がある内容。）

### 中文翻译

（上面短文的中文翻译）

### 📌 单词标注

短文中使用的今日单词（按出现顺序）：

| # | 単語 | 假名 | 意思 |
|---|------|------|------|
| 1 | 高校 | こうこう | 高中 |
| 2 | 間 | かん | 间，期间 |
| ... | ... | ... | ... |

---

## 📝 今日总结

| 统计 | 数据 |
|------|------|
| 今日新词 | N 个 |
| 累计进度 | XXX / 10168 |
| 完成率 | X.X% |
| 当前阶段 | Phase X - JLPT XX |

---

[← back to Japanese](./) | [← back to Other](..) | [← back to home](/)
```

**Key Points:**
- Audio links use relative paths: `./filename.mp3`
- Footer navigation is required
- Each word is a numbered `##` section with a horizontal rule separator
- Furigana in example sentences: 漢字（かんじ）
- Summary table at the end
- Short story at the end uses **ALL** of today's words naturally

### 4.5. Compose Short Story (今日短文)

After generating all vocabulary cards, compose a **short story / essay** that naturally incorporates **ALL** of today's words.

**Story Guidelines:**
- Use **every single word** from today's batch — no exceptions
- The story should be coherent and natural — not a forced word list
- Match difficulty to the current JLPT level (simpler stories for N5, more complex for N1)
- Length: 200–400 characters for N5/N4, 300–600 characters for N3+
- **Do NOT include furigana** in parentheses like 漢字（かんじ） — write plain Japanese only. The TTS audio script strips （） annotations before synthesis, but writing them causes double-reading in audio.
- Provide full Chinese translation below the story
- Add a word annotation table listing all today's words in order of appearance
- The story section goes **before** the summary table in the markdown output

**Story Themes (vary daily):**
- Daily life scenes (shopping, cooking, commuting)
- School / workplace episodes
- Travel / adventure stories
- Seasonal events / Japanese culture
- Conversations between characters

### 5. Generate Audio Files

After generating the markdown file, create audio files using `edge-tts`.

**Command**:

```bash
.venv-audio/bin/python .agent/skills/japanese-learning/scripts/generate_audio.py pages/other/japanese/YYYY-MM-DD_jaNNN.md
```

**Output**: For each vocabulary file, generates:
- `{filename}-words.mp3` — All words read aloud (word + reading)
- `{filename}-sentences.mp3` — All example sentences read aloud
- `{filename}-story.mp3` — Short story read aloud

**Voice**: `ja-JP-NanamiNeural` (natural Japanese female voice)

**Setup** (one-time, shared with english-learning):

```bash
# Reuse existing virtual environment
# If not exists:
python -m venv .venv-audio
.venv-audio/bin/pip install edge-tts
```

**Note**: Audio generation requires an internet connection for edge-tts.

### 6. Update Progress

After successfully generating the markdown and audio files:

1. Update `data/progress.yaml` with:
   - `current_line`: next line to read
   - `last_updated`: today's date
   - `days_completed`: increment by 1
   - Append to `history` list: date, day_number, start_line, end_line, word_count, level, file

### 7. Session Complete

Display a brief summary to the user:
- How many words were generated
- Current progress percentage
- Link to the generated page
- Reminder to listen to audio

**IMPORTANT - Link Format**:
- Use **relative paths** for all markdown links in generated files
- Audio files: `./filename.mp3`
- Navigation: `[← back to Japanese](./) | [← back to Other](..) | [← back to home](/)`
- **Never use** `file:///absolute/path` format in generated markdown files

## Important Notes

- **CSV is read-only**: Never modify `notes.csv`
- **Original order**: Words are learned in the CSV's original order (no re-sorting)
- **Random batch size**: Each day randomly picks 28–35 words
- **AI-generated content**: Example sentences and mnemonics are created by AI at generation time
- **Audio reuse**: Uses the same `.venv-audio` environment and `edge-tts` library as english-learning skill
- **Progress tracking**: `progress.yaml` is the single source of truth for current position

## File Organization

```
# Skill files
.agent/skills/japanese-learning/
├── SKILL.md                           # This file
├── data/
│   ├── notes.csv                      # 10,168 words source (CSV)
│   └── progress.yaml                  # Learning progress tracker
└── scripts/
    └── generate_audio.py              # TTS audio generation script

# Generated output (GitHub Pages)
pages/other/japanese/
├── index.md                           # Directory index (auto-lists articles)
├── YYYY-MM-DD_ja001.md                # Day 1 vocabulary
├── YYYY-MM-DD_ja001-words.mp3         # Day 1 word audio
├── YYYY-MM-DD_ja001-sentences.mp3     # Day 1 sentence audio
├── YYYY-MM-DD_ja001-story.mp3         # Day 1 story audio
├── YYYY-MM-DD_ja002.md                # Day 2 vocabulary
├── YYYY-MM-DD_ja002-words.mp3         # Day 2 word audio
├── YYYY-MM-DD_ja002-sentences.mp3     # Day 2 sentence audio
├── YYYY-MM-DD_ja002-story.mp3         # Day 2 story audio
└── ...
```

## Error Handling

- If `progress.yaml` is missing, create a new one starting from line 1
- If CSV file is not found, show error with expected path
- If `.venv-audio` doesn't exist, create it and install `edge-tts`
- If audio generation fails, still save the markdown file and warn the user
- If all words are completed, congratulate and offer to restart
