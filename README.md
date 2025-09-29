# 🏆 YallaKora Match Scraper

[![CI/CD Pipeline](https://github.com/KhalilAmamri/python-beautifulsoup-web-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/KhalilAmamri/python-beautifulsoup-web-scraper/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional Python web scraper that extracts football match data from [YallaKora](https://www.yallakora.com/) for any specified date and saves it to structured CSV files.

---

## ✨ Features

- 🎯 **Smart Date Validation**: Robust date format validation with proper error handling
- 🌐 **Reliable Web Scraping**: Handles dynamic website structure changes
- 🏆 **Multi-Championship Support**: Extracts matches from all available championships
- 📊 **Structured Data Export**: Clean CSV output with proper encoding
- 🔧 **Professional Code Structure**: Object-oriented design with proper error handling
- 📝 **Comprehensive Logging**: Detailed logs for debugging and monitoring
- 🧪 **Unit Tested**: Comprehensive test suite for reliability
- 🚀 **CI/CD Ready**: GitHub Actions integration for automated testing
- 💻 **Command Line Interface**: Easy-to-use CLI with multiple options

---

## 📋 Project Structure

```
python-beautifulsoup-web-scraper/
├── src/
│   ├── yallakora_scraper.py    # Main scraper class
│   └── config.py               # Configuration settings
├── tests/
│   └── test_scraper.py         # Unit tests
├── data/                       # Output CSV files (auto-created)
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── cli.py                      # Command line interface
├── setup.py                    # Package setup
├── requirements.txt            # Dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

---

## 🖥️ Preview

📁 Example CSV output:

```csv
championship;first_team;second_team;score;time
كأس العالم للأندية;الترجى الرياضي;تشيلسي;0 - 3;04:00
كأس العالم للأندية;لوس أنجلوس;فلامنجو;1 - 1;04:00
الدوري المصري;الأهلي;الزمالك;2 - 1;21:00
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/KhalilAmamri/python-beautifulsoup-web-scraper.git
cd python-beautifulsoup-web-scraper
```

### 2. Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Or using the setup script
pip install -e .
```

### 3. Run the Scraper

#### Interactive Mode

```bash
python src/yallakora_scraper.py
```

#### Command Line Interface

```bash
# Scrape specific date
python cli.py --date 29-09-2025

# Scrape today's matches
python cli.py --today

# Scrape yesterday's matches
python cli.py --yesterday

# Custom output directory
python cli.py --date 29-09-2025 --output my_data

# Verbose logging
python cli.py --date 29-09-2025 --verbose
```

---

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=src --cov-report=html
```

---

## 📊 Code Quality

This project maintains high code quality standards:

```bash
# Install development tools
pip install black isort flake8 mypy

# Format code
black src/
isort src/

# Lint code
flake8 src/

# Type checking
mypy src/ --ignore-missing-imports
```

---

## 🔧 Configuration

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

Available configuration options:

- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `OUTPUT_DIR`: Directory for CSV files
- `REQUEST_TIMEOUT`: HTTP request timeout in seconds

---

## 📦 Requirements

- **Python**: 3.8+ (tested on 3.8, 3.9, 3.10, 3.11, 3.12, 3.13)
- **Dependencies**:
  - `requests` >= 2.31.0
  - `beautifulsoup4` >= 4.12.0
  - `lxml` >= 4.9.0
- **Internet Connection**: Required for web scraping

---

## 🛠️ Technologies Used

- **Python 3.8+** 🐍
- **Web Scraping**: `requests` + `BeautifulSoup4`
- **Data Processing**: `csv`, `pandas-compatible`
- **Testing**: `pytest`, `unittest`
- **CI/CD**: GitHub Actions
- **Code Quality**: `black`, `isort`, `flake8`, `mypy`

---

## 📈 Recent Improvements

- ✅ **Fixed Dynamic Class Names**: Now handles changing CSS class names
- ✅ **Enhanced Error Handling**: Comprehensive exception handling
- ✅ **Professional Structure**: Object-oriented design
- ✅ **Comprehensive Testing**: Unit tests with good coverage
- ✅ **CI/CD Integration**: Automated testing and quality checks
- ✅ **Command Line Interface**: Multiple usage options
- ✅ **Logging System**: Detailed logging for debugging

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/python-beautifulsoup-web-scraper.git
cd python-beautifulsoup-web-scraper

# Install in development mode
pip install -e .
pip install -r requirements.txt

# Install development tools
pip install pytest black isort flake8 mypy

# Run tests
pytest tests/
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Important Notes

- **Website Dependency**: This scraper depends on YallaKora's website structure
- **Rate Limiting**: Be respectful with requests to avoid being blocked
- **Legal Compliance**: Ensure you comply with the website's terms of service
- **Data Usage**: Use scraped data responsibly and ethically

---

## 🆘 Support

If you encounter any issues:

1. **Check the logs**: Look at `scraper.log` for detailed error information
2. **Review Issues**: Check [GitHub Issues](https://github.com/KhalilAmamri/python-beautifulsoup-web-scraper/issues)
3. **Create an Issue**: Provide detailed information about the problem
4. **Community**: Join discussions and help others

---

## 🌟 Show Your Support

If this project helped you, please ⭐ **star** the repository and consider:

- 🍴 **Forking** the project
- 📝 **Contributing** improvements
- 🐛 **Reporting** bugs
- 💡 **Suggesting** new features

---

**Made with ❤️ by [Khalil Amemri](https://github.com/KhalilAmamri)**
