# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 9:33
# @Author  : Jaywatson
# @File    : sqlUtil.py
# @Soft    : back_python
import os
import sqlite3
import sys
from pathlib import Path

class sqlUtil:
    def __init__(self, filePath):
        self.file = filePath
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        path = str(Path(self.path + self.file))
        if not os.path.exists(path):
           conn = sqlite3.connect(path)
           print(1)