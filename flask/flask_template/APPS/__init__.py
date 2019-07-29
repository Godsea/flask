from flask import Flask,escape
from .ext import init_ext
from APPS.views import init_view
import os
from APPS.settings import app_type


# 注册app
def create_app(pro_env):
    app = Flask(__name__, static_url_path='', root_path=os.path.abspath(''))
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@172.16.0.206:3306/aa"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(app_type.get(pro_env) or 'default')
    init_ext(app=app)
    init_view(app=app)

    return app


