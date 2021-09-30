# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 18:15
# @Author  : Jaywatson
# @File    : code.py
# @Soft    : backend_flask

class ResponseCode(object):
    SUCCESS = 200  # 成功

    #权限相关
    BROKENTOKEN = 'A0001' # token内容异常
    INVALIDTOKEN = 'A0002'  # token为空或者非法
    TOKENERROR = 'A0003' # token校验异常

    #系统工具类
    JWTERROR = 'U0001' # JWT工具类异常

    #未知异常
    EXCEPTION = 'E9999' # 位置异常
