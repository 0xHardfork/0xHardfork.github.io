import json
from pathlib import Path

history_path = Path("/Users/peigen/Documents/dev/0xHardfork/0xHardfork.github.io/.agent/skills/english-learning/data/history.json")
with open(history_path, 'r', encoding='utf-8') as f:
    history = json.load(f)

new_session = {
  "date": "2026-03-15",
  "difficulty": "intermediate",
  "scenarios": [
    {
      "name": "API Integration Planning",
      "type": "meeting",
      "category": "it"
    },
    {
      "name": "DevSecOps Pipeline",
      "type": "casual",
      "category": "it"
    },
    {
      "name": "Travel Planning",
      "type": "casual",
      "category": "daily"
    }
  ],
  "vocabulary_count": {
    "english": 0,
    "japanese": 0
  }
}

history["sessions"].append(new_session)

with open(history_path, 'w', encoding='utf-8') as f:
    json.dump(history, f, indent=2, ensure_ascii=False)
