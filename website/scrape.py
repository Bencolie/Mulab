from website import categories, get_tracks, download
from flask import Blueprint,render_template

scrape = Blueprint('scrape',__name__)

@scrape.route('/music_categories')
def music_categories():
    return render_template('scrape.html',categories=categories)

@scrape.route('/music_trcaks') 
def music_tracks():
    return 'Music_Tracks'