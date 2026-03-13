---
name: article-translation
description: Article translation skill that translates user-provided Chinese articles into native-quality English and Japanese. Outputs a sentence-by-sentence side-by-side comparison (Chinese | English and Chinese | Japanese) and generates audio files. Use when user provides an article and asks for translation.
---

# Article Translation Skill

This skill translates a Chinese article into native-quality English and Japanese. The output is a sentence-by-sentence side-by-side comparison table and audio files for pronunciation practice.

## When to use this skill

- User provides a Chinese article (or any text) and asks for translation into English and/or Japanese
- User says "帮我翻译", "翻译这篇文章", "translate this article"
- User provides a passage and says "生成英文和日文版本"

## Workflow

### 1. Receive Input

受け取った記事を確認する:

1. User pastes a Chinese article (paragraph or multi-paragraph text)
2. If the article is very long (>50 sentences), ask user if they want to process it in parts or all at once
3. Confirm the target languages (default: both English 🇺🇸 and Japanese 🇯🇵)

### 2. Split Into Sentences

Split the article into individual sentences. Rules:

- Split on Chinese sentence-ending punctuation: `。`, `！`, `？`, `……`, `；`
- Keep closely related short phrases together if splitting them would lose meaning
- Remove leading/trailing whitespace from each sentence
- Assign a sequential number to each sentence (1, 2, 3, ...)

### 3. Translate — English Version

Translate each Chinese sentence into **native-speaker English**. Requirements:

**Core Translation Principles:**

1. **Sound like a native writer**: Use natural English rhythm, not word-for-word translation
2. **Preserve the author's voice**: Match the tone (formal/casual/journalistic/literary)
3. **Use idiomatic expressions**: Choose phrases that native English speakers actually use
4. **Adapt cultural references**: When needed, provide equivalent expressions that carry the same connotation
5. **Sentence structure**: English sentences may be restructured — passive to active, etc. — as long as meaning is preserved

**Style Guidance:**

- ❌ AVOID: Overly literal translations that sound awkward
- ✅ USE: Natural phrasing that reads as if originally written in English
- ❌ AVOID: "He said that he thinks that it is very important"
- ✅ USE: "He stressed its importance" / "He made the point clearly"
- ❌ AVOID: Translating 非常 always as "very" — use: "remarkably", "exceptionally", "incredibly", etc. based on context
- ✅ USE: Varied, rich vocabulary appropriate to the register

### 4. Translate — Japanese Version

Translate each Chinese sentence into **native-speaker Japanese**. Requirements:

**Core Translation Principles:**

1. **自然な日本語**: バイリンガルの母語者が書くような自然な日本語にする
2. **文体の一致**: 原文のトーン (フォーマル/カジュアル/ジャーナリスティック) に合わせる
3. **慣用表現の使用**: 実際の日本語話者が使う表現を選ぶ
4. **文化的適応**: 必要に応じて、同じ意味合いを持つ日本語表現に置き換える
5. **敬語レベル**: 記事の性質に応じて適切な敬語レベルを選ぶ (です/ます or 普通体)

**Style Guidance:**

- ❌ AVOID: 直訳で不自然な日本語
- ✅ USE: 日本語として自然に読める翻訳
- ❌ AVOID: 中国語の構造をそのまま持ち込む
- ✅ USE: 日本語に自然な語順と接続詞

### 5. Generate Output Files

Create two output files in a dated output directory:

**Directory**: `translations/YYYY-MM-DD/`
**If the directory exists for today**, append a numeric suffix: `YYYY-MM-DD-2/`

**File 1**: `{slug}-en.md` — Chinese vs English comparison
**File 2**: `{slug}-ja.md` — Chinese vs Japanese comparison

Where `{slug}` is a brief kebab-case name derived from the article topic (e.g., `climate-change`, `tech-startup`).

---

#### File Format — English (`{slug}-en.md`)

```markdown
# [Article Title or Topic] — English Translation

**Date**: YYYY-MM-DD
**Source Language**: 中文 (Chinese)
**Target Language**: English 🇺🇸

---

## Sentence-by-Sentence Comparison

| # | 中文原文 | English Translation |
|---|---------|---------------------|
| 1 | [Chinese sentence 1] | [English translation 1] |
| 2 | [Chinese sentence 2] | [English translation 2] |
| ... | ... | ... |

---

## Full English Text

[Complete English article as flowing, readable prose — reassemble translated sentences into natural paragraphs]

---

## Translation Notes

> Any notable translation decisions, cultural adaptations, or word choices worth explaining.

---

## 📚 Grammar & Vocabulary Study

### Key Vocabulary

| Word / Phrase | Chinese | CEFR | Definition | 🧠 Mnemonic |
|---------------|---------|------|------------|-------------|
| [word] | [中文] | [A1-C2] | [English definition] | [memorable image, story, or word-association tip] |

### Key Grammar Patterns

| Pattern | Example from Article | 中文说明 |
|---------|---------------------|----------|
| [grammar structure] | [example sentence] | [brief explanation in Chinese] |

### 💡 Article Memory Tips

> [2–4 concrete tips to help memorize the content of this specific article — e.g. a linking story connecting the key points, a visual scene, a numbered hook, or a rhythmic summary sentence]
```

---

#### File Format — Japanese (`{slug}-ja.md`)

```markdown
# [Article Title or Topic] — 日本語訳

**Date**: YYYY-MM-DD
**Source Language**: 中文 (Chinese)
**Target Language**: 日本語 🇯🇵

---

## 一文ずつの対照

| # | 中文原文 | 日本語訳 |
|---|---------|---------|
| 1 | [Chinese sentence 1] | [Japanese translation 1] |
| 2 | [Chinese sentence 2] | [Japanese translation 2] |
| ... | ... | ... |

---

## 全文（日本語）

[完成した日本語の文章 — 翻訳された文を自然なパラグラフに組み立て直したもの]

---

## 翻訳メモ

> 注目すべき翻訳上の判断、文化的な適応、または説明が必要な語句選択。

---

## 📚 文法・語彙学習

### 重要語彙

| 単語／表現 | 假名 | 中文 | CEFR | 意味 | 🧠 記憶術 |
|-----------|------|------|------|------|----------|
| [単語] | [かな] | [中文] | [A1-C2] | [日本語の定義] | [語呂合わせ・イメージ・連想など記憶に残るヒント] |

### 重要文法パターン

| 文法パターン | 記事からの例文 | 中文説明 |
|------------|--------------|----------|
| [文法構造] | [例文] | [中国語で簡単な説明] |

### 💡 記事を覚えるコツ

> [この記事の内容を記憶するための具体的なヒント 2〜4つ — キーポイントをつなぐストーリー、視覚的なシーン、番号フック、リズムのある要約文など]
```

---

### 5.5 Generate Grammar & Vocabulary Study Section

For **each output file** (both `-en.md` and `-ja.md`), generate a **📚 Grammar & Vocabulary Study** section at the end.

#### Key Vocabulary Table

Extract **8–15 of the most valuable words or phrases** from the article. Prioritize:

- Words that appear multiple times or are central to the article's meaning
- Idioms, collocations, or expressions that are hard to guess from context
- Words at B1 level or above (tag with CEFR level)

For each word, provide a **🧠 Mnemonic** — a creative, memorable device to help retention. Use one of these techniques:

| Technique | Example |
|-----------|---------|
| **Visual image** | *"Ephemeral" — imagine a soap bubble labeled 'EPHEM' that vanishes instantly"* |
| **Word-root story** | *"Benevolent" — bene (good) + volent (wish) = wishing good to others"* |
| **Sound-alike (谐音)** | *"Resign" sounds like '里签' — signing your name on something inside"* |
| **Sentence hook** | *Make a short absurd sentence that forces the word's meaning to stick"* |
| **Chinese connection** | *Link the sound or meaning to a familiar Chinese word or concept"* |

#### Key Grammar Patterns Table

Identify **3–5 notable grammar structures** used in the article. For each:

- Name the pattern (e.g. "Inverted conditional", "Nominalization", "Emphatic do")
- Quote the exact example sentence from the article
- Explain in Chinese why this structure is used and what it conveys

#### 💡 Article Memory Tips

Write **2–4 concrete tips** specific to THIS article's content:

- A **linking story**: connect the article's key points into a narrative chain (A → B → C)
- A **visual scene**: paint a mental image that encodes the core message
- A **numbered hook**: "3 things to remember: (1)... (2)... (3)..."
- A **rhythmic summary**: a short rhyme or alliterative phrase capturing the gist

### 6. Generate Audio Files

After generating the markdown files, create audio versions for listening practice:

**Tool**: Use `edge-tts` via the bundled script

**Command** (run from the project root):

```bash
# Generate both English and Japanese audio for all files in a translation output directory
.venv-audio/bin/python .agent/skills/article-translation/scripts/generate_audio.py translations/YYYY-MM-DD/

# Or for a single file
.venv-audio/bin/python .agent/skills/article-translation/scripts/generate_audio.py translations/YYYY-MM-DD/{slug}-en.md
```

**Output**: For each translation file, generates:

- `{slug}-en-audio.mp3` — Full English article read aloud (natural narrator voice)
- `{slug}-ja-audio.mp3` — Full Japanese article read aloud (natural narrator voice)

**Voice selection**:

- English: `en-US-JennyNeural` (warm, natural, neutral accent)
- Japanese: `ja-JP-NanamiNeural` (clear, polished, standard Japanese)

**Setup** (one-time, shared with english-learning skill):

```bash
python -m venv .venv-audio
.venv-audio/bin/pip install edge-tts
```

### 7. Create Session Summary

After generating files and audio, create or update `translations/YYYY-MM-DD/README.md`:

```markdown
# Translation Session — YYYY-MM-DD

**Date**: YYYY-MM-DD

## Articles Translated

| File | Topic | Sentences | Languages |
|------|-------|-----------|-----------|
| [{slug}-en.md](./{slug}-en.md) | [topic] | [N] | English |
| [{slug}-ja.md](./{slug}-ja.md) | [topic] | [N] | Japanese |

## Audio Files

| File | Language |
|------|----------|
| [{slug}-en-audio.mp3](./{slug}-en-audio.mp3) | English |
| [{slug}-ja-audio.mp3](./{slug}-ja-audio.mp3) | Japanese |

## Study Sections

| File | Study Content |
|------|---------------|
| [{slug}-en.md](./{slug}-en.md) | Vocabulary, grammar patterns, memory tips (English) |
| [{slug}-ja.md](./{slug}-ja.md) | 語彙、文法パターン、記憶術 (Japanese) |
```

## Important Notes

- **Native quality is mandatory**: Translations must read as if originally written by a native speaker — never as a direct word-for-word translation
- **Sentence alignment**: Each row in the table must correspond to the same unit of meaning in both languages — some Chinese sentences may map to slightly restructured English/Japanese sentences
- **Full text section**: The "Full Text" section should be polished flowing prose, not just the table rows joined together. Re-read and refine for natural paragraph flow
- **Mnemonics must be creative**: Generic mnemonics ("just repeat it") are useless. Every mnemonic must have a concrete image, story, or hook that makes the word unforgettable
- **Study section is always included**: Generate the Grammar & Vocabulary Study section for every output file, even if the user did not explicitly ask
- **Link format**: Always use **relative paths** for all markdown links (e.g., `./filename.md`), never absolute `file:///` paths
- **Audio is optional**: If the user doesn't need audio, skip Step 6

## File Organization

```text
english/
├── .agent/
│   └── skills/
│       └── article-translation/
│           ├── SKILL.md            ← this file
│           └── scripts/
│               └── generate_audio.py
└── translations/
    └── YYYY-MM-DD/
        ├── README.md
        ├── {slug}-en.md            ← Chinese vs English table + study section
        ├── {slug}-ja.md            ← Chinese vs Japanese table + study section
        ├── {slug}-en-audio.mp3     ← English audio
        └── {slug}-ja-audio.mp3     ← Japanese audio
```
