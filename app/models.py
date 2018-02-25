#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数据库模型类

from app import db
import uuid


class Shares(db.Model):
    __tablename__ = 'tb_shares'  # 指定表名

    id = db.Column(db.String(36), primary_key=True)
    shares_num = db.Column(db.String(36), index=True, unique=True)
    shares_href = db.Column(db.String(36), index=True, unique=True)
    shares_name = db.Column(db.String(36), index=True, unique=True)
    create_time = db.Column(db.DateTime)

    def __init__(self, shares_num, shares_href, shares_name, create_time):
        self.id = uuid.uuid1().__str__()
        self.shares_num = shares_num
        self.shares_href = shares_href
        self.shares_name = shares_name
        self.create_time = create_time


class SharesDetailed(db.Model):
    __tablename__ = 'tb_shares_detailed'  # 指定表名

    id = db.Column(db.String(36), primary_key=True)
    shares_id = db.Column(db.String(36), index=True, unique=True)
    create_time = db.Column(db.DateTime)
    open_price = db.Column(db.Integer)
    close_price = db.Column(db.Integer)
    ceilling_price = db.Column(db.Integer)
    floor_price = db.Column(db.Integer)
    rise_and_fall_range = db.Column(db.Integer)
    rise_and_fall_quota = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    turn_volume = db.Column(db.Integer)
    turnover_rate = db.Column(db.Integer)
    amplitude = db.Column(db.Integer)
    p_e_ratio = db.Column(db.Integer)
    state = db.Column(db.SmallInteger)

    def __init__(self, shares_id, state):

        self.shares_id = shares_id
        self.state = state


