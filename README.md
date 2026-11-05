# Mulab - Web-Based Music Scraping & Streaming Platform

Mulab is a full-stack web application designed to scrape, store, manage, and stream music tracks. Built with a modular Python backend and a responsive frontend interface, the platform integrates automated web scraping pipelines, relational database management, and an interactive web-based media player.

---

## 🚀 Key Features & Workflow

- **Automated Music Scraping:** Implements custom web scraping modules to fetch audio tracks and metadata from target sources.
- **Database Management:** Utilizes structured SQL models (`models.py`) to store song metadata, artist details, and track references securely.
- **Modular Backend Architecture:** Built on Flask using the Application Factory and Blueprint pattern (`views.py`, `genre.py`, `lab.py`) for clean separation of concerns.
- **Web-Based Music Player:** Interactive frontend interface allowing users to browse music genres, view track libraries, and stream audio directly in the browser.
- **Dynamic Frontend Rendering:** Leverages HTML5, JavaScript, and Jinja2 templates (`base.html`, `home.html`, `genre.html`, `lab.html`) for a seamless user experience.

---

## 🛠️ Tech Stack

- **Backend & Scraping:** Python 3, Flask, SQLAlchemy, Web Scraping libraries
- **Frontend:** Jinja2 Templates, HTML5, CSS3, JavaScript (Audio Player API)
- **Database:** SQLite / Relational Database (managed via `models.py`)
- **Tools & Environment:** Git, Python Virtual Environment

---

## 📂 Repository Structure

```text
Mulab/
├── main.py                # Application entry point & server launcher
└── website/               # Core application package
    ├── __init__.py        # App initialization & extension setup
    ├── models.py          # Database models for tracks, artists, and metadata
    ├── views.py           # Core HTTP routes & controller views
    ├── genre.py           # Blueprint for music genre management
    ├── lab.py             # Blueprint for experimental features / scraper triggers
    ├── static/            # Static assets (CSS stylesheets, JS, downloaded audio files)
    └── templates/         # Jinja2 view templates
        ├── base.html      # Global layout wrapper & navigation bar
        ├── home.html      # Homepage & featured track dashboard
        ├── genre.html     # Genre-based track browser
        └── lab.html       # Interactive music player & laboratory interface
