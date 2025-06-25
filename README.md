
# 🏆 YallaKora Match Scraper

A Python script that scrapes football match data from [YallaKora](https://www.yallakora.com/) for a user-specified date and saves it to a structured CSV file.

---

## 📌 Features

- ✅ Validates user input for date format (`dd-mm-yyyy`)
- 🌐 Connects to YallaKora's match center for that date
- 🧠 Parses match info using BeautifulSoup
- 📋 Extracts:
  - Championship name
  - Team A and Team B
  - Match result
  - Match time
- 💾 Saves results to a CSV file in `utf-8-sig` format

---

## 🖥️ Preview

📁 Example saved CSV:

```csv
championship;first_team;second_team;score;time
الدوري المصري;الأهلي;الزمالك;2 - 1;21:00
...
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/yallakora-match-scraper.git
cd yallakora-match-scraper
```

### 2. Install Requirements

```bash
pip install requests beautifulsoup4 lxml
```

### 3. Run the Script

```bash
python scraper.py
```

Enter the date in this format:

```bash
please enter the date in  format: dd-mm-yyyy: 25-06-2025
```

📂 Output will be saved to:

```bash
C:\Learn Programming\python-beautifulsoup-web-scraper\matches_25-06-2025.csv
```

---

## 📦 Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`
- `lxml`
- Internet connection

---

## 🛠 Technologies Used

- Python 🐍
- Web Scraping (requests + BeautifulSoup)
- CSV File Handling

---

## ⚠️ Notes

- Only works if YallaKora’s website structure hasn't changed.
- Scraper currently processes the first championship block only (`championships[0]`).

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests and stars are always welcome ⭐.  
Feel free to fork the repo and submit a PR!
