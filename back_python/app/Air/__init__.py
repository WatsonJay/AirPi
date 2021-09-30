# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 10:33
# @Author  : Jaywatson
# @File    : __init__.py
# @Soft    : back_python

from flask import Blueprint

testBp = Blueprint("test", __name__, url_prefix="/v1/air/")