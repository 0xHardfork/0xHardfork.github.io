#!/usr/bin/env python3
"""
Update history tracking for English learning sessions.
Records completed scenarios to avoid repetition.
"""

import json
import os
from datetime import datetime
from pathlib import Path

class HistoryManager:
    """Manages learning history and statistics."""
    
    def __init__(self, history_file=".agent/skills/english-learning/data/history.json"):
        self.history_file = Path(history_file)
        self.history = self._load_history()
    
    def _load_history(self):
        """Load history from JSON file."""
        if not self.history_file.exists():
            return {
                "sessions": [],
                "statistics": {
                    "total_sessions": 0,
                    "total_dialogues": 0,
                    "scenarios_completed": {}
                }
            }
        
        with open(self.history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_history(self):
        """Save history to JSON file."""
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
    
    def add_session(self, date, scenarios, difficulty):
        """
        Add a new session to history.
        
        Args:
            date: Session date (YYYY-MM-DD)
            scenarios: List of scenario dictionaries with name, type, category
            difficulty: Difficulty level (elementary/intermediate/advanced)
        """
        session = {
            "date": date,
            "scenarios": scenarios,
            "difficulty": difficulty,
            "timestamp": datetime.now().isoformat()
        }
        
        self.history["sessions"].append(session)
        
        # Update statistics
        stats = self.history["statistics"]
        stats["total_sessions"] += 1
        stats["total_dialogues"] += len(scenarios)
        
        # Track scenario usage
        for scenario in scenarios:
            scenario_name = scenario["name"]
            if scenario_name not in stats["scenarios_completed"]:
                stats["scenarios_completed"][scenario_name] = 0
            stats["scenarios_completed"][scenario_name] += 1
        
        self._save_history()
        print(f"✓ Session added to history: {date}")
    
    def get_recent_scenarios(self, days=7):
        """Get scenarios used in the last N days."""
        recent_scenarios = []
        
        for session in reversed(self.history["sessions"][-days:]):
            for scenario in session["scenarios"]:
                recent_scenarios.append({
                    "name": scenario["name"],
                    "date": session["date"],
                    "category": scenario.get("category", "unknown")
                })
        
        return recent_scenarios
    
    def get_scenario_frequency(self, scenario_name):
        """Get how many times a scenario has been used."""
        return self.history["statistics"]["scenarios_completed"].get(scenario_name, 0)
    
    def get_statistics(self):
        """Get overall statistics."""
        return self.history["statistics"]
    
    def print_recent_usage(self, days=7):
        """Print recent scenario usage."""
        recent = self.get_recent_scenarios(days)
        
        if not recent:
            print(f"No scenarios used in the last {days} days.")
            return
        
        print(f"\nRecent scenarios (last {days} days):")
        for item in recent:
            print(f"  - {item['name']} ({item['category']}) on {item['date']}")

def main():
    """Main function for testing."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python update_history.py <action> [args...]")
        print("Actions:")
        print("  add <date> <scenario_name> <type> <category> <difficulty>")
        print("  recent [days]")
        print("  stats")
        return
    
    manager = HistoryManager()
    action = sys.argv[1]
    
    if action == "add":
        # Add a session
        date = sys.argv[2]
        scenario = {
            "name": sys.argv[3],
            "type": sys.argv[4],
            "category": sys.argv[5]
        }
        difficulty = sys.argv[6] if len(sys.argv) > 6 else "intermediate"
        manager.add_session(date, [scenario], difficulty)
        
    elif action == "recent":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        manager.print_recent_usage(days)
        
    elif action == "stats":
        stats = manager.get_statistics()
        print("\nStatistics:")
        print(f"  Total sessions: {stats['total_sessions']}")
        print(f"  Total dialogues: {stats['total_dialogues']}")
        print(f"  Unique scenarios: {len(stats['scenarios_completed'])}")
        print("\nMost practiced scenarios:")
        sorted_scenarios = sorted(
            stats['scenarios_completed'].items(),
            key=lambda x: x[1],
            reverse=True
        )
        for name, count in sorted_scenarios[:5]:
            print(f"  - {name}: {count} times")

if __name__ == "__main__":
    main()
