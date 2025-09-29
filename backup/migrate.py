#!/usr/bin/env python3
"""
Migration script to update from old to new project structure
"""

import os
import shutil

def migrate_project():
    """Migrate from old structure to new structure"""
    print("🚀 Migrating YallaKora Scraper to new structure...")
    
    # Replace old README with new one
    if os.path.exists("README_new.md"):
        if os.path.exists("README.md"):
            shutil.move("README.md", "README_old.md")
            print("📝 Backed up old README.md to README_old.md")
        
        shutil.move("README_new.md", "README.md")
        print("📄 Updated README.md with new content")
    
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
        print("📁 Created data/ directory")
    
    # Move old CSV files to data directory
    csv_files = [f for f in os.listdir(".") if f.startswith("matches_") and f.endswith(".csv")]
    for csv_file in csv_files:
        if not os.path.exists(os.path.join("data", csv_file)):
            shutil.move(csv_file, os.path.join("data", csv_file))
            print(f"📊 Moved {csv_file} to data/ directory")
    
    # Create __init__.py files for Python packages
    init_files = ["src/__init__.py", "tests/__init__.py"]
    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('"""Package initialization"""')
            print(f"📦 Created {init_file}")
    
    print("\n✅ Migration completed successfully!")
    print("\n📋 Next steps:")
    print("1. Test the new CLI: python cli.py --help")
    print("2. Run the scraper: python cli.py --today")
    print("3. Run tests: pytest tests/ -v")
    print("4. Commit and push changes to GitHub")

if __name__ == "__main__":
    migrate_project()