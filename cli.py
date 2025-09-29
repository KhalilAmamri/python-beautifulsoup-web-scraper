#!/usr/bin/env python3
"""
Command Line Interface for YallaKora Scraper

Usage:
    python cli.py --date 29-09-2025
    python cli.py --date 29-09-2025 --output custom_folder
    python cli.py --help
"""

import argparse
import sys
import os
from datetime import datetime, timedelta

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.yallakora_scraper import YallaKoraScraper


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="YallaKora Football Match Scraper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --date 29-09-2025
  python cli.py --date 29-09-2025 --output my_data
  python cli.py --today
  python cli.py --yesterday
        """
    )
    
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument(
        '--date', '-d',
        type=str,
        help='Date to scrape in dd-mm-yyyy format'
    )
    date_group.add_argument(
        '--today',
        action='store_true',
        help='Scrape matches for today'
    )
    date_group.add_argument(
        '--yesterday',
        action='store_true',
        help='Scrape matches for yesterday'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='data',
        help='Output directory for CSV files (default: data)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    return parser.parse_args()


def get_date_string(args):
    """Get date string based on arguments"""
    if args.today:
        return datetime.now().strftime('%d-%m-%Y')
    elif args.yesterday:
        yesterday = datetime.now() - timedelta(days=1)
        return yesterday.strftime('%d-%m-%Y')
    else:
        return args.date


def main():
    """Main CLI function"""
    args = parse_arguments()
    
    # Get date
    date = get_date_string(args)
    
    # Initialize scraper
    scraper = YallaKoraScraper(output_dir=args.output)
    
    if args.verbose:
        import logging
        logging.getLogger().setLevel(logging.DEBUG)
    
    print(f"🏆 YallaKora Match Scraper")
    print(f"📅 Scraping matches for: {date}")
    print(f"📁 Output directory: {args.output}")
    print("-" * 50)
    
    # Scrape matches
    success = scraper.scrape_matches(date)
    
    if success:
        print(f"✅ Successfully scraped matches for {date}!")
        print(f"📄 Check the '{args.output}' folder for the CSV file.")
    else:
        print(f"❌ Failed to scrape matches for {date}.")
        print("💡 Try a different date or check your internet connection.")
        sys.exit(1)


if __name__ == "__main__":
    main()