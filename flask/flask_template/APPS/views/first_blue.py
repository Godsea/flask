from flask import Blueprint, render_template

blue = Blueprint('blue',__name__)


@blue.route('/', methods=['GET','POST'])
def test():
    return render_template('index.html')