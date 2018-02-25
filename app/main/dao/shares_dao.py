# -*- coding: utf-8 -*-
from app import db


def insert_shares(shares):
    db.session.add(shares)
    db.session.commit()


