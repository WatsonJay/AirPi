# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 18:00
# @Author  : Jaywatson
# @File    : ResponseBody.py
# @Soft    : backend_flask
from flask import current_app
from libs.Response.code import ResponseCode


class ResMsg:

    def __init__(self, code = ResponseCode.SUCCESS, data = None):
        self._code = code
        self._data = data
        lang = current_app.config['LANG']
        self._msg = current_app.config[lang].get(code, "")

    def update(self, code=ResponseCode.SUCCESS, data=None):
        self._code = code
        if data is not None:
            self._data = data
        lang = current_app.config['LANG']
        self._msg = current_app.config[lang].get(code, "")

    def add_field(self, name=None, value=None):
        if name is not None and value is not None:
            self.__dict__[name] = value

    def data(self):
        body = self.__dict__
        body["code"] = body.pop("_code")
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["success"] = True
        return body

    def errorData(self):
        body = self.__dict__
        body["code"] = body.pop("_code")
        body.pop("_data")
        body["msg"] =  body.pop("_msg")
        body["success"] = False
        return body