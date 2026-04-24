---
name: japanese-grammar
description: Daily Japanese grammar learning skill that generates grammar study pages from parsed grammar data with explanations, examples, and audio. Use when user says "开始今日语法学习" or wants to start their daily Japanese grammar practice. ~80-day plan covering ~797 grammar points (N4+N3 → N1).
---

# Japanese Grammar Learning Skill

This skill helps you learn Japanese grammar daily through structured grammar cards generated from a curated grammar database (797 grammar points covering JLPT N4+N3 → N1).

## When to use this skill

- User says "开始今日日语语法学习" or "begin today's Japanese grammar study"
- User says "start daily Japanese grammar" or "開始日語語法學習"
- User wants to begin their daily Japanese grammar practice
- User wants to create a new grammar learning session

## Data Source

- **CSV File**: `.agent/skills/japanese-grammar/data/grammar.csv`
- **Total Grammar Points**: 797
- **Columns**: `id`, `level`, `grammar_point`, `connection`, `meaning`, `examples` (JSON array)
- **Levels** (learning order):
  1. `N4+N3` — 217 points (基础)
  2. `N2` — 181 points
  3. `N2~N1` — 169 points (混合)
  4. `N1` — 230 points

## Study Plan

- **Grammar points per day**: **10** (fixed)
- **Order**: Original CSV order (sequential by level)
- **No review mechanism** — pure forward progress
- **Total duration**: ~80 days (~2.5 months)

| Phase | Duration | Level | Grammar Points |
|-------|----------|-------|----------------|
| Phase 1 | ~22 days | N4+N3 | 217 |
| Phase 2 | ~18 days | N2 | 181 |
| Phase 3 | ~17 days | N2~N1 | 169 |
| Phase 4 | ~23 days | N1 | 230 |

## Workflow

### 1. Check Progress

1. **Read progress**: Load `data/progress.yaml` from **this skill's directory** (`.agent/skills/japanese-grammar/data/progress.yaml`)
2. Determine `current_line` — the next CSV line to read (1-indexed, line 1 = header)
3. If `current_line` > 797, congratulate the user — all grammar points completed!
4. **Check today's date**: If a file with today's date already exists in `pages/other/japanese-grammar/`, ask user if they want to overwrite or skip

### 2. Read Grammar Points from CSV

1. Open `.agent/skills/japanese-grammar/data/grammar.csv`
2. Read **10** rows starting from `current_line` (skip header row)
3. If fewer than 10 rows remain, read all remaining rows
4. Parse each row: `id`, `level`, `grammar_point`, `connection`, `meaning`, `examples` (JSON)

### 3. Generate Grammar Content

For each grammar point, the AI must generate:

| Field | Source | Description |
|-------|--------|-------------|
| 文法 (Grammar) | CSV `grammar_point` | 文法パターン |
| 接続 (Connection) | CSV `connection` | 接続規則 (conjugation rule) |
| 意味 (Meaning) | CSV `meaning` | 中文解释 |
| Level | CSV `level` | JLPT 分级 |
| 助记 (Mnemonic) | **AI Generated** | 记忆技巧、逻辑拆解或情境联想 |
| 例句 (Examples) | **AI Generated** | 3-4 natural examples with Chinese translations |
| 使用ポイント (Usage Tips) | **AI Generated** | 使用要点、常见搭配、易混淆语法 |

**Example Sentence Guidelines:**
- Must be natural, daily-use Japanese
- Difficulty should match the grammar point's JLPT level
- **Do NOT include furigana** in parentheses like 漢字（かんじ） — the TTS audio will read both kanji and reading, causing double-reading. Write plain Japanese only: 漢字
- Provide Chinese translation
- Use the target grammar point naturally in context
- Generate **3-4 distinct examples** to cover different use cases

**Mnemonic (助记) Guidelines:**
- Explain the logic behind the grammar point (e.g., character meanings)
- Provide a memorable scenario or sound association
- Compare with English or Chinese patterns if helpful
- Keep it short and catchy (1-2 sentences)

**Usage Tips Guidelines:**
- Highlight common mistakes learners make
- Compare with similar grammar patterns when applicable
- Note formality level (formal/informal/written/spoken)
- Keep tips concise (2-3 bullet points max)

### 4. Generate Markdown File

**Output location**: `pages/other/japanese-grammar/`
**Naming convention**: `YYYY-MM-DD_grNNN.md` where NNN is the day number (001, 002, ...)

**IMPORTANT — Jekyll Front-matter**:

Every generated `.md` file MUST begin with Jekyll front-matter:

```yaml
---
layout: default
title: "Day NNN - JLPT XX 日语文法"
---
```

**File Template:**

```markdown
---
layout: default
title: "Day NNN - JLPT XX 日语文法"
---

# 📖 Day NNN — 日语文法学習

📅 YYYY-MM-DD | 📊 进度: XXX/797 (X.X%) | 🎯 Level: JLPT XX

[🔊 例句朗读](./YYYY-MM-DD_grNNN-examples.mp3) | [🔊 短文朗读](./YYYY-MM-DD_grNNN-passage.mp3)

---

## 1. ～一方だ

| 項目 | 内容 |
|------|------|
| 文法 | ～一方だ |
| 接続 | 用言連体形＋一方だ |
| 意味 | 一直～；越来越～ |
| Level | N2 |

**助记**: 「一方」表示一个方向，动作像在独木桥上一路走到底，不停下。

**例句**:
1. 人口は増える一方だ。 [🔊](./YYYY-MM-DD_grNNN-examples.mp3)
   > 人口一直在增加。
2. 最近、物価は上がる一方で困っている。 [🔊](./YYYY-MM-DD_grNNN-examples.mp3)
   > 最近物价一直在涨，很困扰。
3. 彼の成績は下がる一方だ。 [🔊](./YYYY-MM-DD_grNNN-examples.mp3)
   > 他的成绩一直在下降。

**使用ポイント:**
- 多用于描述单方向持续变化的趋势（通常指不好的方向）
- 常见搭配：増える一方、減る一方、悪くなる一方
- 类似文法：～ばかりだ（也表示持续变化）

---

## 2. ～上に

| 項目 | 内容 |
|------|------|
| 文法 | ～上に |
| 接続 | 体言の｜用言連体形＋うえに |
| 意味 | 而且，又 |
| Level | N2 |

...

---

## 📖 今日短文

以下短文包含了今天学习的所有文法，通过语境帮助你加深记忆。

[🔊 短文朗读](./YYYY-MM-DD_grNNN-passage.mp3)

### 日本語

（AI が今日の文法を全て使って書いた短い文章。自然な日本語で、ストーリー性がある内容。）

### 中文翻译

（上面短文的中文翻译）

### 📌 文法標注

短文中使用的今日文法（按出现顺序）：

| # | 文法 | 意味 |
|---|------|------|
| 1 | ～一方だ | 一直～；越来越～ |
| 2 | ～上に | 而且，又 |
| ... | ... | ... |

---

## 📝 今日总结

| 统计 | 数据 |
|------|------|
| 今日文法 | 10 个 |
| 累计进度 | XXX / 797 |
| 完成率 | X.X% |
| 当前阶段 | Phase X - JLPT XX |

---

[← back to Grammar](./) | [← back to Other](..) | [← back to home](/)
```

**Key Points:**
- Audio links use relative paths: `./filename.mp3`
- Footer navigation is required
- Each grammar point is a numbered `##` section with a horizontal rule separator
- **Do NOT include furigana** in AI-generated examples — write plain Japanese only
- Summary table at the end
- Short passage uses **ALL** of today's grammar points naturally

### 4.5. Compose Short Passage (今日短文)

After generating all grammar cards, compose a **short passage / essay** that naturally incorporates **ALL** of today's grammar points.

**Passage Guidelines:**
- Use **every single grammar point** from today's batch — no exceptions
- The passage should be coherent and natural — not forced
- Match difficulty to the current JLPT level
- Length: 300–600 characters
- **Do NOT include furigana** in parentheses — write plain Japanese only
- Provide full Chinese translation below
- Add a grammar annotation table listing all today's grammar points in order of appearance
- The passage section goes **before** the summary table in the markdown output

**Passage Themes (vary daily):**
- Daily life scenes (shopping, cooking, commuting)
- School / workplace episodes
- Travel / adventure stories
- Seasonal events / Japanese culture
- News / social commentary (for N1 level)

### 5. Generate Audio Files

After generating the markdown file, create audio files using `edge-tts`.

**Command**:

```bash
.venv-audio/bin/python .agent/skills/japanese-grammar/scripts/generate_audio.py pages/other/japanese-grammar/YYYY-MM-DD_grNNN.md
```

**Output**: For each grammar file, generates:
- `{filename}-examples.mp3` — All example sentences read aloud
- `{filename}-passage.mp3` — Short passage read aloud

**Voice**: `ja-JP-NanamiNeural` (natural Japanese female voice)

**Setup** (one-time, shared with other skills):

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
   - Append to `history` list: date, day_number, start_line, end_line, grammar_count, level, file

### 7. Session Complete

Display a brief summary to the user:
- How many grammar points were generated
- Current progress percentage
- Link to the generated page
- Reminder to listen to audio

**IMPORTANT - Link Format**:
- Use **relative paths** for all markdown links in generated files
- Audio files: `./filename.mp3`
- Navigation: `[← back to Grammar](./) | [← back to Other](..) | [← back to home](/)`
- **Never use** `file:///absolute/path` format in generated markdown files

## Important Notes

- **CSV is read-only**: Never modify `grammar.csv`
- **Original order**: Grammar is learned in CSV's original order (no re-sorting)
- **Fixed batch size**: Each day covers exactly 10 grammar points (last day may have fewer)
- **AI-generated content**: Extra examples and usage tips are created by AI at generation time
- **Audio reuse**: Uses the same `.venv-audio` environment and `edge-tts` library as other skills
- **Progress tracking**: `progress.yaml` is the single source of truth for current position

## File Organization

```
# Skill files
.agent/skills/japanese-grammar/
├── SKILL.md                           # This file
├── data/
│   ├── grammar.csv                    # 797 grammar points (parsed CSV)
│   └── progress.yaml                  # Learning progress tracker
└── scripts/
    └── generate_audio.py              # TTS audio generation script

# Generated output (GitHub Pages)
pages/other/japanese-grammar/
├── index.md                           # Directory index
├── YYYY-MM-DD_gr001.md                # Day 1 grammar
├── YYYY-MM-DD_gr001-examples.mp3      # Day 1 example audio
├── YYYY-MM-DD_gr001-passage.mp3       # Day 1 passage audio
└── ...
```

## Error Handling

- If `progress.yaml` is missing, create a new one starting from line 1
- If CSV file is not found, show error with expected path
- If `.venv-audio` doesn't exist, create it and install `edge-tts`
- If audio generation fails, still save the markdown file and warn the user
- If all grammar points are completed, congratulate and offer to restart
