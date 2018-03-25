# -*- coding: utf-8 -*-
from app import app
from app import models
from app.main.dao import shares_dao
import time


@app.route('/insertShares/<shares_num>/<shares_name>')
def insert_shares(shares_num, shares_name):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当地时间

    shares = models.Shares(shares_num,'htttp://....', shares_name, now)
    try:

        # shares_dao.insert_shares(shares)
        print("message")
    except Exception as e:
        print(e)
        return "failed"

    return "success"
