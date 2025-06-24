import requests
from bs4 import BeautifulSoup
import csv


date = input("please enter the date in YYYY-MM-DD format: ")
page = requests.get(f"https://www.yallakora.com/Match-Center?date={date}")
# this will be the URL for the match center page of YallaKora for the given date
