# Mulab - Automated Music Scraping & Streaming Web Architecture
<img width="1440" height="776" alt="Capture d’écran 2026-11-06 à 12 21 02" src="https://github.com/user-attachments/assets/ab727af2-4ff2-4479-a088-96381c6d1b04" />



Mulab is a full-stack Python web application engineered for automated music scraping, relational database persistence, dynamic web playback, and genre management. 

The system features an automated **Selenium Headless Scraping Pipeline** to bypass complex DOM/cookie overlays and extract music tracks (with Dropbox download integration), paired with a **Microsoft SQL Server (MSSQL)** backend and a **modular Flask Blueprints** web architecture.

---

## 🚀 Key Technical Highlights & Architecture

- **Automated Scraping Pipeline (Selenium):**
  - Runs Chrome in `--headless` mode for automated web navigation and data parsing.
  - Handles dynamic DOM elements using explicit waits (`WebDriverWait`, `EC.element_to_be_clickable`).
  - Automatically handles cookie banners, complex SVG modals, and extracts audio track links (Dropbox integration).
  - Implements an automated local file downloader for retrieved audio assets.
- **Database Integration (MSSQL & SQLAlchemy):**
  - Configured with `SQLAlchemy` ORM via `pyodbc` (ODBC Driver 17 / FreeTDS) to interface with **Microsoft SQL Server**.
  - Implements a self-healing connection verification routine (`check_connection()`) and automatic schema creation.
- **Modular Flask Application (Application Factory Pattern):**
  - Built using `create_app()` factory pattern for scalable configurations.
  - Divided into modular Blueprints: `views` (Core application), `genre` (Genre classification), and `lab` (Experimental features & scraper triggers).
  - Integrated **Flask-CORS** to enable seamless cross-origin communication between API endpoints and frontend players.

---

## 🛠️ Tech Stack & Dependencies

- **Backend & Web Framework:** Python 3, Flask, Flask-CORS, Flask-SQLAlchemy
- **Automated Web Scraping:** Selenium WebDriver, Chrome Driver
- **Database Engine:** Microsoft SQL Server (MSSQL), `pyodbc` driver
- **Frontend Architecture:** HTML5, CSS3, JavaScript, Jinja2 Template Engine

---

## 📂 Repository Architecture

```text
Mulab/
├── main.py                # Application entry point & server runner
├── DockerFile
├── docker-compose.yml
├── requirements.txt
└── website/               # Core application package
    ├── __init__.py        # App Factory (Selenium scrapers, MSSQL setup, Blueprints)
    ├── models.py          # Database models (Tracks, Genres)
    ├── views.py           # Core HTTP routes & controller views
    ├── genre.py           # Music genre classification Blueprint
    ├── lab.py             # Laboratory / Experimental trigger Blueprint
    ├── static/            # Static stylesheets, JS audio player scripts, local downloads
    └── templates/         # Jinja2 view templates
        ├── base.html      # Layout wrapper & navigation bar
        ├── home.html      # Homepage & featured track dashboard
        ├── genre.html     # Genre-based track browser
        └── lab.html       # Interactive player & scraper control panel
```

---

## 🏁 Getting Started & Setup

### Prerequisites

1. **Python 3.8+** installed on your system.
2. **Google Chrome** browser and a compatible **ChromeDriver** executable.
3. **Microsoft SQL Server (MSSQL)** instance running locally or remotely (with ODBC Driver 17 for SQL Server installed).

### Installation & Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bencolie/Mulab.git
   cd Mulab
   ```

2. **Build docker container with docker compose:**
     ```bash
     docker compose up --build -d
     ```

3. **Configure Database Credentials & Driver Path:**
   Open `website/__init__.py` and update the MSSQL connection properties and local ChromeDriver path according to your environment:
   ```python
   # Update server & database details
   server = 'YOUR_SERVER_NAME'
   database = 'YOUR_DATABASE_NAME'
   username = 'sa'
   password = 'YOUR_PASSWORD'

   # Ensure ChromeDriver executable path is correct in get_website()
   new_driver = r'YOUR_LOCAL_CHROMEDRIVER_PATH'
   ```

   Navigate to `http://127.0.0.1:4000` in your web browser to access the web interface, trigger scraping pipelines, and stream audio tracks. Use `Control + C` or `docker compose down` to exit and remove the docker container. 

---

## 📌 Technical Summary for Engineering Reviewers

- Demonstrates robust handling of **asynchronous dynamic web elements** and **automated data ingestion**.
- Implements production-ready **MVC design patterns** separating ETL/scraping tasks, SQL database schemas, and view templates.
