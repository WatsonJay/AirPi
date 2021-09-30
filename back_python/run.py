# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 9:50
# @Author  : Jaywatson
# @File    : run.py
# @Soft    : back_python
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    # print(f"load `{env_path}` environment file")
    load_dotenv(env_path)

from libs import create_app

app = create_app(path=os.path.dirname(__file__))
app.app_context().push()