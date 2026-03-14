#!/usr/bin/env python3
"""
Archive vocabulary from daily dialogues to cumulative vocabulary lists.
Filters words by CEFR level based on difficulty setting.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set


class VocabularyArchiver:
    """Manages vocabulary archiving with CEFR-based filtering."""
    
    # CEFR filtering rules based on difficulty
    CEFR_FILTERS = {
        'elementary': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'],  # A1 and above - all levels
        'intermediate': ['B1', 'B2', 'C1', 'C2'],             # B1 and above
        'advanced': ['B2', 'C1', 'C2']                        # B2-C2 only
    }
    
    def __init__(self, vocab_base_path='vocabulary'):
        self.vocab_base_path = Path(vocab_base_path)
        self.english_archive = self.vocab_base_path / 'english' / 'vocabulary.md'
        self.japanese_archive = self.vocab_base_path / 'japanese' / 'vocabulary.md'
        
    def extract_vocabulary_from_dialogue(self, dialogue_file: Path, language: str) -> List[Dict]:
        """
        Extract vocabulary table from a dialogue markdown file.
        
        Args:
            dialogue_file: Path to dialogue markdown file
            language: 'english' or 'japanese'
            
        Returns:
            List of vocabulary dictionaries with keys: word, definition, cefr_level, example
        """
        if not dialogue_file.exists():
            print(f"Warning: File not found: {dialogue_file}")
            return []
        
        with open(dialogue_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        vocabulary = []
        
        if language == 'english':
            # Find English vocabulary section
            vocab_section = re.search(
                r'### Vocabulary\s*\n\n.*?\n\n\|(.*?)\n\|(.*?)\n((?:\|.*?\n)+)',
                content,
                re.DOTALL
            )
            if vocab_section:
                header = vocab_section.group(1).strip()
                separator = vocab_section.group(2).strip()
                rows = vocab_section.group(3).strip().split('\n')
                
                for row in rows:
                    parts = [p.strip() for p in row.split('|')]
                    if len(parts) >= 5 and parts[1]:  # Has word content
                        vocabulary.append({
                            'word': parts[1],
                            'definition': parts[2],
                            'cefr_level': parts[3],
                            'example': parts[4]
                        })
        
        elif language == 'japanese':
            # Find Japanese vocabulary section
            vocab_section = re.search(
                r'### 語彙 \(Vocabulary\)\s*\n\n.*?\n\n\|(.*?)\n\|(.*?)\n((?:\|.*?\n)+)',
                content,
                re.DOTALL
            )
            if vocab_section:
                header = vocab_section.group(1).strip()
                separator = vocab_section.group(2).strip()
                rows = vocab_section.group(3).strip().split('\n')
                
                for row in rows:
                    parts = [p.strip() for p in row.split('|')]
                    if len(parts) >= 6 and parts[1]:  # Has word content
                        vocabulary.append({
                            'word': parts[1],
                            'definition': f"{parts[2]} ({parts[3]})",
                            'cefr_level': parts[4],
                            'example': parts[5]
                        })
        
        return vocabulary
    
    def filter_by_cefr(self, vocabulary: List[Dict], difficulty: str) -> List[Dict]:
        """
        Filter vocabulary by CEFR level based on difficulty setting.
        
        Args:
            vocabulary: List of vocabulary dictionaries
            difficulty: 'elementary', 'intermediate', or 'advanced'
            
        Returns:
            Filtered vocabulary list
        """
        if difficulty not in self.CEFR_FILTERS:
            print(f"Warning: Unknown difficulty '{difficulty}', using 'intermediate'")
            difficulty = 'intermediate'
        
        allowed_levels = self.CEFR_FILTERS[difficulty]
        filtered = []
        
        for word_entry in vocabulary:
            cefr = word_entry.get('cefr_level', '').strip().upper()
            if cefr in allowed_levels:
                filtered.append(word_entry)
        
        return filtered
    
    def get_existing_words(self, archive_file: Path, language: str) -> Set[str]:
        """
        Get set of words already in the archive to prevent duplicates.
        
        Args:
            archive_file: Path to vocabulary archive file
            language: 'english' or 'japanese'
            
        Returns:
            Set of words already archived
        """
        if not archive_file.exists():
            return set()
        
        existing_words = set()
        
        with open(archive_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract table rows
        table_match = re.search(r'\|.*?\|\n\|[-:\s|]+\|\n((?:\|.*?\n)*)', content, re.DOTALL)
        if table_match:
            rows = table_match.group(1).strip().split('\n')
            for row in rows:
                parts = [p.strip() for p in row.split('|')]
                if len(parts) >= 2 and parts[1]:  # Has word
                    existing_words.add(parts[1].lower())
        
        return existing_words
    
    def append_to_archive(
        self,
        vocabulary: List[Dict],
        archive_file: Path,
        language: str,
        source_scenario: str,
        date: str
    ):
        """
        Append vocabulary to archive file, avoiding duplicates.
        
        Args:
            vocabulary: List of vocabulary dictionaries to add
            archive_file: Path to archive file
            language: 'english' or 'japanese'
            source_scenario: Name of the scenario this vocabulary came from
            date: Date in YYYY-MM-DD format
        """
        # Get existing words
        existing_words = self.get_existing_words(archive_file, language)
        
        # Filter out duplicates
        new_words = [
            word for word in vocabulary
            if word['word'].lower() not in existing_words
        ]
        
        if not new_words:
            print(f"No new {language} vocabulary to add (all words already exist)")
            return
        
        # Read current content
        with open(archive_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the table and insert new rows before the final separator
        table_pattern = r'(\|.*?\|\n\|[-:\s|]+\|\n(?:\|.*?\n)*)(---)'
        
        new_rows = []
        for word in new_words:
            row = f"| {word['word']} | {word['definition']} | {word['cefr_level']} | {word['example']} | {date} | {source_scenario} |"
            new_rows.append(row)
        
        new_rows_text = '\n'.join(new_rows) + '\n'
        
        # Update content
        content = re.sub(
            table_pattern,
            r'\1' + new_rows_text + r'\2',
            content,
            count=1
        )
        
        # Update timestamp and total count
        content = re.sub(
            r'\*\*Last Updated:\*\* .*',
            f'**Last Updated:** {date}',
            content
        )
        
        # Update word count
        total_updated = len(existing_words) + len(new_words)
        content = re.sub(
            r'\*Total words: \d+\*',
            f'*Total words: {total_updated}*',
            content
        )
        
        # Write back
        with open(archive_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added {len(new_words)} new {language} words to archive")
    
    def archive_session_vocabulary(
        self,
        dialogue_files: List[Path],
        difficulty: str,
        date: str
    ):
        """
        Archive vocabulary from a session's dialogue files.
        
        Args:
            dialogue_files: List of paths to dialogue markdown files
            difficulty: Current difficulty level
            date: Session date in YYYY-MM-DD format
        """
        print(f"\nArchiving vocabulary (Difficulty: {difficulty})...")
        print(f"CEFR levels to archive: {', '.join(self.CEFR_FILTERS.get(difficulty, []))}")
        print()
        
        all_english_vocab = []
        all_japanese_vocab = []
        
        # Extract vocabulary from all dialogue files
        for dialogue_file in dialogue_files:
            if not dialogue_file.exists():
                continue
            
            scenario_name = dialogue_file.stem
            print(f"Processing: {dialogue_file.name}")
            
            # Extract English vocabulary
            english_vocab = self.extract_vocabulary_from_dialogue(dialogue_file, 'english')
            if english_vocab:
                all_english_vocab.extend(english_vocab)
                print(f"  Found {len(english_vocab)} English words")
            
            # Extract Japanese vocabulary
            japanese_vocab = self.extract_vocabulary_from_dialogue(dialogue_file, 'japanese')
            if japanese_vocab:
                all_japanese_vocab.extend(japanese_vocab)
                print(f"  Found {len(japanese_vocab)} Japanese words")
        
        print()
        
        # Filter by CEFR level
        filtered_english = self.filter_by_cefr(all_english_vocab, difficulty)
        filtered_japanese = self.filter_by_cefr(all_japanese_vocab, difficulty)
        
        print(f"After CEFR filtering:")
        print(f"  English: {len(filtered_english)} words")
        print(f"  Japanese: {len(filtered_japanese)} words")
        print()
        
        # Append to archives
        if filtered_english:
            self.append_to_archive(
                filtered_english,
                self.english_archive,
                'english',
                'Multiple scenarios',
                date
            )
        else:
            print("No English vocabulary to archive")
        
        if filtered_japanese:
            self.append_to_archive(
                filtered_japanese,
                self.japanese_archive,
                'japanese',
                'Multiple scenarios',
                date
            )
        else:
            print("No Japanese vocabulary to archive")
        
        print("\n✓ Vocabulary archiving complete!")


def main():
    """Main function for command-line usage."""
    if len(sys.argv) < 4:
        print("Usage: python archive_vocabulary.py <difficulty> <date> <dialogue_file1> [dialogue_file2] ...")
        print()
        print("Arguments:")
        print("  difficulty    : elementary, intermediate, or advanced")
        print("  date          : Session date (YYYY-MM-DD)")
        print("  dialogue_files: One or more dialogue markdown files")
        print()
        print("Example:")
        print("  python archive_vocabulary.py intermediate 2026-01-31 2026-01-31/dialogue1.md 2026-01-31/dialogue2.md")
        return
    
    difficulty = sys.argv[1]
    date = sys.argv[2]
    dialogue_files = [Path(f) for f in sys.argv[3:]]
    
    archiver = VocabularyArchiver()
    archiver.archive_session_vocabulary(dialogue_files, difficulty, date)


if __name__ == '__main__':
    main()
