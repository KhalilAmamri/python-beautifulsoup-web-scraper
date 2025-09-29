"""Simple YallaKora Match Scraper

Usage:
    python scraper.py

Enter a date like: 29-09-2025
CSV saved to: data/matches_<date>.csv
"""

from __future__ import annotations

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os


def validate_date(date_text: str) -> bool:
    """Return True if date is in dd-mm-yyyy format and valid."""
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def format_for_url(date_text: str) -> str:
    d = datetime.strptime(date_text, "%d-%m-%Y")
    # YallaKora expects m/d/YYYY (no leading zeros)
    return f"{d.month}/{d.day}/{d.year}"


def fetch_page(date_text: str) -> BeautifulSoup | None:
    url = f"https://www.yallakora.com/match-center?date={format_for_url(date_text)}"
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        return BeautifulSoup(resp.content, "lxml")
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None


def extract_matches(soup: BeautifulSoup) -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []

    # Championship cards: div.matchCard.matchesList (their first class has a number, we ignore it)
    championship_cards = soup.select("div.matchCard.matchesList")
    if not championship_cards:
        return matches

    for card in championship_cards:
        title_el = card.find("h2")
        if not title_el:
            continue
        championship_name = title_el.get_text(strip=True)

        match_items = card.select(
            "div.item.finish.liItem, div.item.future.liItem, div.item.now.liItem"
        )

        for m in match_items:
            team_a_el = m.select_one("div.teams.teamA")
            team_b_el = m.select_one("div.teams.teamB")
            if not team_a_el or not team_b_el:
                continue

            team_a = team_a_el.get_text(strip=True)
            team_b = team_b_el.get_text(strip=True)

            result_box = m.select_one("div.MResult")
            score = "- - -"
            match_time = "-"
            if result_box:
                score_spans = result_box.select("span.score")
                if len(score_spans) >= 2:
                    left = score_spans[0].get_text(strip=True)
                    right = score_spans[1].get_text(strip=True)
                    score = f"{left} - {right}"
                time_el = result_box.select_one("span.time")
                if time_el:
                    match_time = time_el.get_text(strip=True)

            matches.append(
                {
                    "championship": championship_name,
                    "first_team": team_a,
                    "second_team": team_b,
                    "score": score,
                    "time": match_time,
                }
            )

    return matches


def save_csv(date_text: str, rows: list[dict[str, str]]) -> str:
    os.makedirs("data", exist_ok=True)
    filename = os.path.join("data", f"matches_{date_text}.csv")
    if not rows:
        return ""
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f, fieldnames=["championship", "first_team", "second_team", "score", "time"], delimiter=";"
        )
        writer.writeheader()
        writer.writerows(rows)
    return filename


def main() -> None:
    while True:
        date_text = input("Enter date (dd-mm-yyyy): ").strip()
        if validate_date(date_text):
            break
        print("Invalid date. Please try again.")

    soup = fetch_page(date_text)
    if not soup:
        print("Could not get page. Exiting.")
        return

    matches = extract_matches(soup)
    if not matches:
        print(f"No matches found for {date_text}.")
        return

    out = save_csv(date_text, matches)
    if out:
        print(f"Saved {len(matches)} matches to {out}")
    else:
        print("No data to save.")


if __name__ == "__main__":
    main()