#!/usr/bin/env python3
"""
Initialize daily English learning task.
Creates a dated directory and session structure.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

def get_today_dir_name():
    """Get directory name for today (YYYY-MM-DD format)."""
    return datetime.now().strftime("%Y-%m-%d")

def create_daily_directory(base_path="."):
    """
    Create daily directory with today's date.
    Returns the path to the created directory.
    """
    base_path = Path(base_path)
    today = get_today_dir_name()
    daily_dir = base_path / today
    
    # Check if directory already exists
    if daily_dir.exists():
        # Check for alternative numbering
        counter = 2
        while True:
            alt_dir = base_path / f"{today}-{counter}"
            if not alt_dir.exists():
                daily_dir = alt_dir
                break
            counter += 1
        
        print(f"Directory {today}/ already exists.")
        print(f"Creating alternative directory: {daily_dir.name}/")
    
    # Create directory
    daily_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Created directory: {daily_dir}")
    
    return daily_dir

def create_index_file(daily_dir):
    """Create initial index.md file in daily directory."""
    index_path = daily_dir / "index.md"
    
    today = datetime.now().strftime("%Y-%m-%d")
    content = f"""# English Learning Session - {today}

**Date**: {today}  
**Status**: In Progress

## Scenarios Selected

### IT/Computer Scenario
- **Scenario**: [To be selected]
- **Type**: [Meeting/Casual]
- **File**: [To be generated]

### Daily Life Scenario
- **Scenario**: [To be selected]
- **Type**: [Meeting/Casual]
- **File**: [To be generated]

## Session Notes

[Add any notes about today's learning session here]

---

## Statistics

- **Dialogues Completed**: 0/2
- **Total Exchanges**: 0
- **New Vocabulary**: 0
"""
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created index file: {index_path}")
    return index_path

def main():
    """Main function."""
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "."
    
    print("Initializing daily English learning task...")
    print()
    
    # Create daily directory
    daily_dir = create_daily_directory(base_path)
    
    # Create index file
    create_index_file(daily_dir)
    
    print()
    print("✓ Daily task initialized successfully!")
    print(f"  Directory: {daily_dir}")
    print()
    print("Next steps:")
    print("1. Select your IT scenario")
    print("2. Select your daily life scenario")
    print("3. Choose dialogue types for each")
    print("4. Generate dialogues")
    
    return str(daily_dir)

if __name__ == "__main__":
    main()
