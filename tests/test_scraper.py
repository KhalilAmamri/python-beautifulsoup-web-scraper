"""
Unit tests for YallaKora Scraper
"""

import unittest
import os
import sys
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.yallakora_scraper import YallaKoraScraper


class TestYallaKoraScraper(unittest.TestCase):
    """Test cases for YallaKoraScraper class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scraper = YallaKoraScraper(output_dir="test_data")
    
    def tearDown(self):
        """Clean up after tests"""
        # Remove test files if they exist
        test_file = os.path.join("test_data", "matches_01-01-2025.csv")
        if os.path.exists(test_file):
            os.remove(test_file)
        
        # Remove test directory if empty
        if os.path.exists("test_data") and not os.listdir("test_data"):
            os.rmdir("test_data")
    
    def test_validate_date_format_valid(self):
        """Test valid date formats"""
        valid_dates = ["01-01-2025", "29-02-2024", "31-12-2023"]
        for date in valid_dates:
            with self.subTest(date=date):
                self.assertTrue(self.scraper.validate_date_format(date))
    
    def test_validate_date_format_invalid(self):
        """Test invalid date formats"""
        invalid_dates = [
            "1-1-2025",      # Single digits
            "01/01/2025",    # Wrong separator
            "2025-01-01",    # Wrong order
            "32-01-2025",    # Invalid day
            "01-13-2025",    # Invalid month
            "invalid",       # Not a date
            "",              # Empty string
        ]
        for date in invalid_dates:
            with self.subTest(date=date):
                self.assertFalse(self.scraper.validate_date_format(date))
    
    def test_format_date_for_url(self):
        """Test date formatting for URL"""
        test_cases = [
            ("01-01-2025", "1/1/2025"),
            ("29-02-2024", "2/29/2024"),
            ("31-12-2023", "12/31/2023"),
        ]
        for input_date, expected in test_cases:
            with self.subTest(date=input_date):
                result = self.scraper.format_date_for_url(input_date)
                self.assertEqual(result, expected)
    
    @patch('src.yallakora_scraper.requests.Session.get')
    def test_get_page_content_success(self, mock_get):
        """Test successful page content retrieval"""
        # Mock successful response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.scraper.get_page_content("01-01-2025")
        
        self.assertIsNotNone(result)
        mock_get.assert_called_once()
    
    @patch('src.yallakora_scraper.requests.Session.get')
    def test_get_page_content_failure(self, mock_get):
        """Test failed page content retrieval"""
        # Mock failed response
        mock_get.side_effect = Exception("Network error")
        
        result = self.scraper.get_page_content("01-01-2025")
        
        self.assertIsNone(result)
    
    def test_save_to_csv_empty_data(self):
        """Test saving empty match data"""
        result = self.scraper.save_to_csv([], "01-01-2025")
        self.assertFalse(result)
    
    def test_save_to_csv_with_data(self):
        """Test saving match data to CSV"""
        test_data = [
            {
                'championship': 'Test Championship',
                'first_team': 'Team A',
                'second_team': 'Team B',
                'score': '2 - 1',
                'time': '20:00'
            }
        ]
        
        result = self.scraper.save_to_csv(test_data, "01-01-2025")
        self.assertTrue(result)
        
        # Check if file was created
        expected_file = os.path.join("test_data", "matches_01-01-2025.csv")
        self.assertTrue(os.path.exists(expected_file))


class TestScraperIntegration(unittest.TestCase):
    """Integration tests for the scraper"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scraper = YallaKoraScraper(output_dir="test_integration")
    
    def tearDown(self):
        """Clean up after tests"""
        # Clean up test directory
        import shutil
        if os.path.exists("test_integration"):
            shutil.rmtree("test_integration")
    
    @unittest.skip("Requires internet connection and actual website")
    def test_full_scraping_process(self):
        """Test the complete scraping process with a real date"""
        # This test requires internet connection and working website
        result = self.scraper.scrape_matches("29-09-2025")
        
        # Result could be True (matches found) or False (no matches)
        # Both are valid outcomes
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    # Create test runner with verbose output
    unittest.main(verbosity=2)