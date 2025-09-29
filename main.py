#!/usr/bin/env python3
"""
YallaKora Match Scraper - Main Entry Point

This is the main file you can run to use the scraper.
It automatically uses the improved version from the src/ folder.

Usage:
    python main.py
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main scraper
from src.yallakora_scraper import main

if __name__ == "__main__":
    main()