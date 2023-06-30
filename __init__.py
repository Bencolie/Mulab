# Flask & SQL related packages
from flask import Flask
import pyodbc
from flask_sqlalchemy import SQLAlchemy
import os
import urllib.parse
# packages for scraping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# packages for ErrorHandling
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_tracks(url):
    # Run Chrome with headless mode
    options =Options()
    options.add_argument("--headless")

    music = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    music.get(url)
    # Accept cookies
    time.sleep(5)
    music.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/button[1]').click()
    # Close Newsletter Subscription Window (svg-handling)
    WebDriverWait(music, 60).until(EC.element_to_be_clickable((By.XPATH, "//div//div//*[name()='svg' and @aria-hidden='true']"))).click()
    
    container = music.find_element(By.ID,"PAGES_CONTAINER")

    # Trakcs's name List
    trac_names = []
    positions0 = container.find_elements(By.CSS_SELECTOR,"span[class='RMxLCF']")
    for i in range(0,len(positions0)):
        trac_name = positions0[i].find_element(By.CSS_SELECTOR,"span[class^='TrackName3057130458__title']").text
        trac_names.append(trac_name)
    # Dowmload Link
    links=[]
    positions1 = container.find_elements(By.CSS_SELECTOR,"a[data-testid='linkElement']")
    for j in range(0,len(positions1)):
        link = positions1[j].get_attribute('href')
        if link[0:24] == "https://www.dropbox.com/":
            links.append(link)
        else:
            continue
    # Construct a dict
    tracks = {}
    id = 0
    for k in range(0,18):
        id += 1
        tracks[id]={}
        tracks[id]['trakc_name'] = trac_names[k]
        tracks[id]['href'] = links[k]
    return  trac_names,links,tracks

def download(url):
    download=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    download.get(url)

# Run Chrome with headless mode
options =Options()
options.add_argument("--headless")

# Find all music categories on the website 
music = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
music.get('https://www.ashamaluevmusic.com/')
    
# Accept cookies
WebDriverWait(music, 6).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/button[1]"))).click()
# Close Newsletter Subscription Window (svg-handling)
WebDriverWait(music, 65).until(EC.element_to_be_clickable((By.XPATH, "//div//div//*[name()='svg' and @aria-hidden='true']"))).click()
# Construct categories' dict 
categories = {}
id = 0
urls= music.find_elements(By.CSS_SELECTOR,'a[data-testid=''linkElement]')
for i in range(0,len(urls)):
    if urls[i].get_attribute('class')=='kuTaGy wixui-button zKbzSQ':
        id += 1
        categories[id]={}
        categories[id]['cat_name'] = urls[i].find_element(By.TAG_NAME,'span').text
        categories[id]['cat_url'] = urls[i].get_attribute('href')
music.quit()

# SQL set up 
db = SQLAlchemy()
db_name = 'master'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjkskahkd oqpoipjlk' # key is set randomly
    # Build the connction with flask and mssql (driver = FreeTDS)
    app.config['SQLALCHEMY_DATABASE_URI']= "mssql+pyodbc:///?odbc_connect="+ urllib.parse.quote_plus('DRIVER={FreeTDS};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=someThingComplicated1234')    

    db.init_app(app)
    # Verify the mssql connection
    check_connection()

    # register the blueprints
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .scrape import scrape
    app.register_blueprint(scrape, url_prefix='/')
    from .lab import lab
    app.register_blueprint(lab, url_prefix='/')

    # register the database models
    from .models import Tracks
    create_database(app)

    return app


def check_connection():
    try:
        db.session.execute('SELECT 1')
        return 'Connection Successful'
    except Exception as e:
        return f'Connection error:{str(e)}'

def create_database(app):
    db_path = os.path.join('website',db_name)
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    else:
        print('The DataBase has already existed !!')