# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 11:33
# @Author  : Jaywatson
# @File    : GetYaml.py
# @Soft    : backend_flask

import yaml

def read_yaml_file(yaml_file_path):
    config = {}
    try:
        with open(yaml_file_path, 'rb') as file:
            config= yaml.safe_load(file.read())
    except:
        raise ValueError('请输入正确的配置名称或配置文件路径')
    if config != None:
        return config
    else:
        return {}