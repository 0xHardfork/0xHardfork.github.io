# English Learning Skill

A comprehensive English learning skill for daily practice with scenario-based dialogues in multiple languages.

## Overview

This skill helps you practice English through daily scenario-based dialogues with support for:
- 🗣️ **Multi-language output**: Chinese, English, and Japanese (with/without furigana)
- 💼 **IT/Computer scenarios**: Code reviews, meetings, technical discussions
- 🌍 **Daily life scenarios**: Shopping, dining, travel, social activities
- 📚 **Grammar explanations**: Detailed breakdowns of language structures
- 📖 **Vocabulary lists**: Key words and phrases with examples
- 📊 **History tracking**: Avoid repetition and track progress
- 🎯 **Difficulty levels**: Elementary (初级), Intermediate (中级), Advanced (高级)

## Quick Start

When you're ready to begin your daily English practice, simply say:

```
开始今日任务
```

or in English:

```
start today's task
```

The skill will automatically:
1. Create a dated directory (e.g., `2026-01-31/`)
2. Automatically select 3 scenarios (avoiding recent ones):
   - **IT Scenario - Meeting** (formal)
   - **IT Scenario - Casual Communication** (informal)
   - **Daily Life Scenario - Casual Chat** (informal)
3. Show you the selected scenarios for confirmation
4. Generate 3 natural, native-speaker dialogues
5. Provide grammar explanations and vocabulary in all three languages
6. Track your progress to avoid repetition

## Structure

```
.agent/skills/english-learning/
├── SKILL.md                    # Main skill instructions
├── config.yaml                 # Scenario and difficulty configuration
├── data/
│   └── history.json           # Session history and statistics
├── scripts/
│   ├── init_daily_task.py     # Initialize daily directory
│   └── update_history.py      # Track session history
└── resources/
    ├── dialogue_template.md   # Template for dialogue structure
    └── sample_dialogues/      # Example dialogues
        ├── code-review-casual.md
        └── weekend-plans-casual.md
```

## Configuration

Edit `config.yaml` to:
- Add or modify IT scenarios
- Add or modify daily life scenarios
- Change difficulty level: `elementary`, `intermediate`, `advanced`
- Adjust dialogue parameters

### Example Scenarios

**IT/Computer:**
- Code Review Discussion
- Sprint Planning Meeting
- Debugging Session
- Technical Design Discussion
- Stand-up Meeting
- API Integration Planning
- Performance Optimization
- Security Review
- And more...

**Daily Life:**
- Restaurant Ordering
- Weekend Plans
- Travel Planning
- Grocery Shopping
- Coffee Shop Chat
- Movie Discussion
- Doctor's Appointment
- Hotel Check-in
- And more...

## How It Works

### 1. Daily Task Initialization

When you start a daily task, a new directory is created with today's date:

```
2026-01-31/
├── index.md                          # Session summary
├── code-review-meeting.md            # Generated dialogue 1
└── weekend-plans-casual.md           # Generated dialogue 2
```

### 2. Scenario Selection

Choose one scenario from each category:
- **IT/Computer scenario** (e.g., "Code Review Discussion")
- **Daily life scenario** (e.g., "Weekend Plans")

For each scenario, select the dialogue type:
- **会议 (Meeting)** - Formal meeting context
- **日常同事沟通 (Casual)** - Informal communication

### 3. Dialogue Generation

Natural, realistic dialogues are generated with:
- Natural conversation flow (10-15 exchanges)
- Appropriate formality based on context
- Common idioms and expressions
- Vocabulary suited to difficulty level

### 4. Multi-language Content

Each dialogue includes:

**中文版** - Full Chinese translation

**English Version** - With:
- Grammar explanations
- Vocabulary table
- Key phrases

**日本語版（ふりがな付き）** - Japanese with furigana notation  
Example: 今日(きょう)は会議(かいぎ)

**日本語版** - Japanese without furigana, with:
- 文法説明 (Grammar explanations)
- 語彙 (Vocabulary)

### 5. Progress Tracking

History is automatically tracked in `data/history.json`:
- Sessions completed
- Scenarios used
- Statistics and frequency
- Helps avoid repetition

## Difficulty Levels

### 初级 (Elementary)
- Simple sentence structures
- Common, everyday vocabulary
- Clear, easy-to-understand grammar
- Short exchanges

### 中级 (Intermediate)
- More complex sentences
- Varied vocabulary with some technical terms
- Common idioms and expressions
- Natural conversation flow

### 高级 (Advanced)
- Native-level expressions
- Nuanced language and cultural context
- Advanced vocabulary and idioms
- Complex grammar structures

## Example Dialogues

See `resources/sample_dialogues/` for complete examples:
- **code-review-casual.md** - IT scenario, intermediate level
- **weekend-plans-casual.md** - Daily life scenario, elementary level

## Tips for Best Results

1. **Be consistent**: Practice daily for best results
2. **Vary scenarios**: Try different topics to expand vocabulary
3. **Review grammar**: Don't skip the grammar explanations
4. **Practice all languages**: Use the multi-language support to reinforce learning
5. **Track progress**: Check your history to see improvement over time

## Customization

### Adding New Scenarios

Edit `config.yaml` and add to `it_scenarios` or `daily_scenarios`:

```yaml
- name: "Your Scenario Name"
  name_cn: "场景中文名"
  description: "Brief description of the scenario"
```

### Changing Difficulty

Update `config.yaml`:

```yaml
difficulty: elementary  # or intermediate, advanced
```

## Scripts

### Initialize Daily Task
```bash
python scripts/init_daily_task.py
```

### View Recent History
```bash
python scripts/update_history.py recent 7
```

### View Statistics
```bash
python scripts/update_history.py stats
```

## Notes

- Dialogues are designed to sound natural and conversational
- Grammar explanations focus on practical usage
- Vocabulary emphasizes frequently-used words
- Japanese furigana uses the format: 漢字(ひらがな)
- All content is automatically tracked to avoid repetition

## Support

For questions or customization needs, refer to `SKILL.md` for detailed instructions on how the agent uses this skill.

---

**Version**: 1.0  
**Author**: Created with Antigravity  
**License**: Personal use
