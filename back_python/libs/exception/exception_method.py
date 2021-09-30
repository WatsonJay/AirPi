# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 10:43
# @Author  : Jaywatson
# @File    : util_exception.py
# @Soft    : backend_flask

class ExceptionMethod(Exception):
    status_code = 1

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
