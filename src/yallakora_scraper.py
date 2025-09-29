"""
YallaKora Football Match Scraper

A Python script that scrapes football match data from YallaKora website
and saves it to CSV files.

Author: Khalil Amemri
Date: 2025
"""

import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional
import logging


class YallaKoraScraper:
    """Main scraper class for YallaKora website"""
    
    def __init__(self, output_dir: str = "data"):
        """
        Initialize the scraper
        
        Args:
            output_dir (str): Directory to save CSV files
        """
        self.base_url = "https://www.yallakora.com/match-center"
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Setup logging
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('scraper.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def validate_date_format(self, date_text: str) -> bool:
        """
        Validate date format (dd-mm-yyyy)
        
        Args:
            date_text (str): Date string to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            datetime.strptime(date_text, '%d-%m-%Y')
            return True
        except ValueError:
            return False
    
    def format_date_for_url(self, date_text: str) -> str:
        """
        Convert date from dd-mm-yyyy to m/d/yyyy format for URL
        
        Args:
            date_text (str): Date in dd-mm-yyyy format
            
        Returns:
            str: Date in m/d/yyyy format
        """
        day, month, year = date_text.split('-')
        return f"{int(month)}/{int(day)}/{year}"
    
    def get_page_content(self, date: str) -> Optional[requests.Response]:
        """
        Fetch page content for given date
        
        Args:
            date (str): Date in dd-mm-yyyy format
            
        Returns:
            Optional[requests.Response]: Response object or None if failed
        """
        try:
            formatted_date = self.format_date_for_url(date)
            url = f"{self.base_url}?date={formatted_date}"
            
            self.logger.info(f"Fetching data from: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            return response
        except requests.RequestException as e:
            self.logger.error(f"Error fetching page: {e}")
            return None
    
    def extract_match_details(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """
        Extract match details from BeautifulSoup object
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            
        Returns:
            List[Dict[str, str]]: List of match details
        """
        matches_details = []
        
        # Find all championship cards
        championships = soup.find_all("div", class_=lambda x: x and 'matchCard matchesList' in x)
        
        if not championships:
            self.logger.warning("No championships found on the page")
            return matches_details
        
        self.logger.info(f"Found {len(championships)} championships")
        
        for championship in championships:
            try:
                championship_title = championship.contents[1].find("h2")
                if not championship_title:
                    continue
                
                championship_name = championship_title.text.strip()
                
                # Find all match types
                finished_matches = list(championship.contents[3].find_all("div", {'class': 'item finish liItem'}))
                future_matches = list(championship.contents[3].find_all("div", {'class': 'item future liItem'}))
                current_matches = list(championship.contents[3].find_all("div", {'class': 'item now liItem'}))
                all_matches = finished_matches + future_matches + current_matches
                
                self.logger.info(f"Found {len(all_matches)} matches in {championship_name}")
                
                for match in all_matches:
                    match_details = self._extract_single_match(match, championship_name)
                    if match_details:
                        matches_details.append(match_details)
                        
            except Exception as e:
                self.logger.error(f"Error processing championship: {e}")
                continue
        
        return matches_details
    
    def _extract_single_match(self, match_element, championship_name: str) -> Optional[Dict[str, str]]:
        """
        Extract details from a single match element
        
        Args:
            match_element: BeautifulSoup element containing match data
            championship_name (str): Name of the championship
            
        Returns:
            Optional[Dict[str, str]]: Match details or None if failed
        """
        try:
            # Get team names
            team_a_element = match_element.find("div", {'class': 'teams teamA'})
            team_b_element = match_element.find("div", {'class': 'teams teamB'})
            
            if not team_a_element or not team_b_element:
                return None
            
            team_a = team_a_element.text.strip()
            team_b = team_b_element.text.strip()
            
            # Get match result
            result_element = match_element.find("div", {'class': 'MResult'})
            if not result_element:
                return None
            
            score_elements = result_element.find_all("span", {'class': 'score'})
            if len(score_elements) >= 2:
                score = f"{score_elements[0].text.strip()} - {score_elements[1].text.strip()}"
            else:
                score = "- - -"
            
            # Get match time
            time_element = result_element.find("span", {'class': 'time'})
            match_time = time_element.text.strip() if time_element else "TBD"
            
            return {
                'championship': championship_name,
                'first_team': team_a,
                'second_team': team_b,
                'score': score,
                'time': match_time
            }
            
        except Exception as e:
            self.logger.error(f"Error extracting match details: {e}")
            return None
    
    def save_to_csv(self, matches_details: List[Dict[str, str]], date: str) -> bool:
        """
        Save match details to CSV file
        
        Args:
            matches_details (List[Dict[str, str]]): List of match details
            date (str): Date in dd-mm-yyyy format
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not matches_details:
            self.logger.warning("No match details to save")
            return False
        
        try:
            filename = os.path.join(self.output_dir, f"matches_{date}.csv")
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as output_file:
                fieldnames = ['championship', 'first_team', 'second_team', 'score', 'time']
                writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=';')
                
                writer.writeheader()
                writer.writerows(matches_details)
            
            self.logger.info(f"Successfully saved {len(matches_details)} matches to {filename}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving to CSV: {e}")
            return False
    
    def scrape_matches(self, date: str) -> bool:
        """
        Main method to scrape matches for a given date
        
        Args:
            date (str): Date in dd-mm-yyyy format
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.validate_date_format(date):
            self.logger.error("Invalid date format. Please use dd-mm-yyyy format.")
            return False
        
        # Get page content
        response = self.get_page_content(date)
        if not response:
            return False
        
        # Parse HTML
        soup = BeautifulSoup(response.content, "lxml")
        
        # Extract match details
        matches_details = self.extract_match_details(soup)
        
        if not matches_details:
            self.logger.info(f"No matches found for {date}")
            return False
        
        # Save to CSV
        return self.save_to_csv(matches_details, date)


def main():
    """Main function to run the scraper"""
    scraper = YallaKoraScraper()
    
    while True:
        date = input("Please enter the date in format (dd-mm-yyyy): ").strip()
        
        if scraper.validate_date_format(date):
            break
        else:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
    
    # Scrape matches
    success = scraper.scrape_matches(date)
    
    if success:
        print(f"✅ Matches for {date} have been successfully scraped and saved!")
    else:
        print(f"❌ Failed to scrape matches for {date}. Check the logs for details.")


if __name__ == "__main__":
    main()