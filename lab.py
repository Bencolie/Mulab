from flask import Blueprint,render_template,url_for

lab = Blueprint('lab',__name__)

@lab.route('/lab')

def visualiuzation():
    return render_template('lab.html')