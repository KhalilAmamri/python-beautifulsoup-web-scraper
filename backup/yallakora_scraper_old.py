import requests
from bs4 import BeautifulSoup
import csv
import os


def validate_date_format(date_text):
    if len(date_text) != 10:
        return False
    if date_text[2] != '-' or date_text[5] != '-':
        return False
    day, month, year = date_text.split('-')
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    if not (1 <= int(day) <= 31):
        return False
    if not (1 <= int(month) <= 12):
        return False
    if not (len(year) == 4 and int(year) > 0):
        return False
    return True

date = input("please enter the date in  format: dd-mm-yyyy: ")
while not validate_date_format(date):
    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
    date = input("please enter the date in  format: dd-mm-yyyy: ")

# Convert date from dd-mm-yyyy to m/d/yyyy for the URL parameter
day, month, year = date.split('-')
formatted_date = f"{int(month)}/{int(day)}/{year}"

page = requests.get(f"https://www.yallakora.com/match-center?date={formatted_date}")
# this will be the URL for the match center page of YallaKora for the given date

def main(page):
    src = page.content
    soup =  BeautifulSoup(src, "lxml")
    matches_details = []
    # Find all divs with class containing 'matchCard matchesList'
    championships = soup.find_all("div", class_=lambda x: x and 'matchCard matchesList' in x)
    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2")
        # Convert ResultSets to lists before concatenating
        finished_matches = list(championships.contents[3].find_all("div", {'class': 'item finish liItem'}))
        future_matches = list(championships.contents[3].find_all("div", {'class': 'item future liItem'}))
        current_matches = list(championships.contents[3].find_all("div", {'class': 'item now liItem'}))
        all_matches = finished_matches + future_matches + current_matches
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            # get team names
            team_A = all_matches[i].find("div", {'class': 'teams teamA'}).text.strip()
            team_B = all_matches[i].find("div", {'class': 'teams teamB'}).text.strip()
            # get match score
            match_result = all_matches[i].find("div", {'class': 'MResult'}).find_all("span", {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            # get match time
            match_time = all_matches[i].find("div", {'class': 'MResult'}).find("span", {'class': 'time'}).text.strip()
            # append the match details to the list
            matches_details.append({
                'championship': championship_title.text.strip(),
                'first_team': team_A,
                'second_team': team_B,
                'score': score,
                'time': match_time
            })
            # print(f"Match: {team_A} vs {team_B} | Score: {score} | Time: {match_time} | Championship: {championship_title.text.strip()}")

    if len(championships) == 0:
        print(f"No matches found for {date}. Please check if there are any matches scheduled for this date.")
        return
    
    get_match_info(championships[0])

    if not matches_details:
        print(f"No match details extracted for {date}.")
        return

    # write the match details to a CSV file
    key = matches_details[0].keys()
    
    # Create data directory if it doesn't exist
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Save to data directory
    filename = os.path.join(data_dir, f"matches_{date}.csv")
    with open(filename, 'w', newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, key, delimiter=';')
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print(f"✅ Matches details for {date} have been written to {filename}")

main(page)
