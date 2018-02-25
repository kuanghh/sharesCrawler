#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全局配置文件

import os

basedir = os.path.abspath(os.path.dirname(__file__))  # 首先获得当前文件（比如配置文件）所在的路径

# SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径
# SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹。

# 配置 sqlalchemy 数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/graduation_design?charset=utf8'

# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'


SQLALCHEMY_TRACK_MODIFICATIONS = True