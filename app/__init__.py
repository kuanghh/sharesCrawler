# -*- coding: utf-8 -*-

from flask import Flask  # 引入Flask
# from flask.ext.sqlalchemy import SQLAlchemy  # 这里会报错
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')  # 载入配置文件
db = SQLAlchemy(app)  # 创建数据库对象

from app import views, models  # 这个与 app的顺序不能放反了
from app.main.controller.shares_controller import *
