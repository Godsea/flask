from flask import Blueprint,render_template

second = Blueprint('second',__name__)


@second.route('/test/')
def index():
    return render_template('index.html')


