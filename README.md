# 🏆 YallaKora Match Scraper

# YallaKora Match Scraper (Simple Version)

This is a very simple Python script that gets football match data from the YallaKora website for a date you choose and saves the results into a CSV file inside the `data/` folder.

## ✅ What It Does

- Asks you for a date (format: `dd-mm-yyyy`)
- Downloads the match center page for that date
- Collects all matches (all championships on that day)
- Saves them to: `data/matches_<date>.csv`

## 🗂 Project Structure

```
python-beautifulsoup-web-scraper/
├── scraper.py          # The only script you need to run
├── requirements.txt    # Needed libraries
├── data/               # CSV files will be saved here
├── README.md           # This file
└── LICENSE             # Open-source license
```

## 🚀 How To Use

1. Install Python 3.8 or newer
2. Install the required libraries:

```
pip install -r requirements.txt
```

3. Run the scraper:

```
python scraper.py
```

4. Enter a date when asked (example: `29-09-2025`)
5. Open the `data/` folder to see the CSV file

## 📄 Example CSV Output

```
championship;first_team;second_team;score;time
الدوري المصري;الأهلي;الزمالك;2 - 1;21:00
```

## ❓ FAQ

**Where are the CSV files saved?** In the `data/` folder.

**What if there are no matches?** The script will tell you. No file is created.

**Why is the score sometimes `- - -`?** The match hasn’t been played or no result yet.

## ⚠ Notes

- You need an internet connection.
- If YallaKora changes its website layout, the scraper may stop working.

## 🛠 Requirements

See `requirements.txt`:

```
requests
beautifulsoup4
lxml
```

## 🧾 License

This project is licensed under the MIT License. See `LICENSE`.

---

Made simple for learning. Enjoy! ✅

Note: If you still see folders like `src/`, `tests/`, `.github/`, or files like `setup.py`, `cli.py`, they are leftovers from an older advanced version. You can ignore them or delete them manually. Only `scraper.py`, `requirements.txt`, `data/`, `LICENSE`, and this `README.md` are needed now.
**Made with ❤️ by [Khalil Amamri](https://github.com/KhalilAmamri)**
