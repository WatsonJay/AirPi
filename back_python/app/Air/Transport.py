# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 15:55
# @Author  : Jaywatson
# @File    : Transport.py
# @Soft    : back_python
from libs.Response.body import ResMsg
from util.sql_factory import BaseSql
from app.Air import airBp
from models.EnvData import EnvData

@airBp.route("/getDashData", methods=["GET"])
def getDashData():
    sql = BaseSql(EnvData)
    data = EnvData.query.order_by(EnvData.creatTime.desc()).first()
    datas = sql.parse_data(data)
    res = ResMsg(200, datas)
    return res.data()

@airBp.route("/getHistoryData", methods=["GET"])
def getHistoryData():
    sql = BaseSql(EnvData)
    data = EnvData.query.order_by(EnvData.creatTime).limit(2000).all()
    datas = sql.parse_data(data)
    createtime = []
    hcho = []
    tvoc = []
    co2 = []
    pm25 = []
    pm10 = []
    for data in datas:
        createtime.append(data['creatTime'].strftime('%Y-%m-%d %H:%M:%S'))
        hcho.append(data['hcho']/1000)
        tvoc.append(data['tvoc']/1000)
        co2.append(data['co2'])
        pm25.append(data['pm25'])
        pm10.append(data['pm10'])
    res = ResMsg(200, {
        'createtime': createtime, 'hcho': hcho,
        'tvoc': tvoc, 'co2': co2,
        'pm25': pm25, 'pm10': pm10})
    return res.data()