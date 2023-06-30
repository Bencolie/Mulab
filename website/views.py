# Here stores all the routes of the website
from flask import Blueprint,render_template,url_for

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')