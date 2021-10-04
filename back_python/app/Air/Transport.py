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