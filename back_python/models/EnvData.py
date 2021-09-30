# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 14:38
# @Author  : Jaywatson
# @File    : EnvData.py
# @Soft    : back_python
from libs import db

class EnvData(db.Model):
    __tablename__ = 't_air_env_data'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    creatTime = db.Column(db.DateTime, nullable=False)
    hcho = db.Column(db.Float)
    tvoc = db.Column(db.Float)
    co2 = db.Column(db.Integer)
    pm25 = db.Column(db.Float)
    pm10 = db.Column(db.Float)
    temp = db.Column(db.Integer)
    hum = db.Column(db.Integer)