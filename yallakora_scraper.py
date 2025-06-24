import requests
from bs4 import BeautifulSoup
import csv


date = input("please enter the date in  format: dd-mm-yyyy: ")
page = requests.get(f"https://www.yallakora.com/Match-Center?date={date}")
# this will be the URL for the match center page of YallaKora for the given date

def main(page):
    src = page.content
    soup =  BeautifulSoup(src, "lxml")
    matches_details = []
    championships = soup.find_all("div", {'class' : '2893 matchCard matchesList'})
    def get_match_info(championships):
        championship_title = championships.contents[0].find("h2").text.strip()
        # print(f"Championship: {championship_title}")
    get_match_info(championships[0])

main(page)
