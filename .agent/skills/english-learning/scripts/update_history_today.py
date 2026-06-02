import json
from pathlib import Path

history_path = Path("/Users/peigen/Documents/dev/0xHardfork/0xHardfork.github.io/.agent/skills/english-learning/data/history.json")
with open(history_path, 'r', encoding='utf-8') as f:
    history = json.load(f)

new_session = {
  "date": "2026-06-02",
  "difficulty": "intermediate",
  "scenarios": [
    {
      "name": "Zero Trust Architecture",
      "type": "meeting",
      "category": "it"
    },
    {
      "name": "Deployment Discussion",
      "type": "casual",
      "category": "it"
    },
    {
      "name": "Restaurant Ordering",
      "type": "casual",
      "category": "daily"
    }
  ],
  "vocabulary_count": {
    "english": 18,
    "japanese": 15
  }
}

history["sessions"].append(new_session)

with open(history_path, 'w', encoding='utf-8') as f:
    json.dump(history, f, indent=2, ensure_ascii=False)

print("Successfully updated history.json!")
