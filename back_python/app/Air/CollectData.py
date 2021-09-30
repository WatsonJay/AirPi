# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 10:36
# @Author  : Jaywatson
# @File    : CollectDate.py
# @Soft    : back_python
import random
from datetime import datetime

from models.EnvData import EnvData
from libs import db
from util.sql_factory import BaseSql


def collect():
    with db.app.app_context():
        sql = BaseSql(EnvData)
        sql.insert([{
            'creatTime': datetime.now(),
            'hcho': random.random(),
            'tvoc': random.random(),
            'co2': random.randint(0, 99),
            'pm25': random.random(),
            'pm10': random.random(),
            'temp': random.randint(0, 99),
            'hum': random.randint(0, 99)
        }])
        print("----------------test------------------")