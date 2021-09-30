    # -*- coding: utf-8 -*-
# @Time    : 2020/12/15 10:30
# @Author  : Jaywatson
# @File    : exception_handler.py
# @Soft    : backend_flask
from flask import Blueprint

from libs.Response.body import ResMsg
from libs.exception.exception_method import ExceptionMethod

exception = Blueprint('exception',__name__)

@exception.app_errorhandler(ExceptionMethod)
def ExceptionHandler(error):
    res = ResMsg(error.status_code)
    return res.errorData()

@exception.app_errorhandler(Exception)
def ExceptionHandler(error):
    res = ResMsg('E9999')
    return res.errorData()

