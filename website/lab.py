from flask import Blueprint,render_template

lab = Blueprint('lab',__name__)

@lab.route('/music_lab')

def visualiuzation():
    return render_template('lab.html')