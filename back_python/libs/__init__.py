# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 17:16
# @Author  : Jaywatson
# @File    : __init__.py
# @Soft    : back_python
import logging
import logging.config
import os
from flask import Flask

from libs.exception.exception_handler import exception
from libs.core import scheduler_init, register_api, db
from util import get_yaml

def create_app(**kwargs):
    try:
        app = Flask(__name__)

        # 加载配置文件
        config = None
        langConfig = get_yaml.read_yaml_file("conf/msg.yaml")
        commonConfig = get_yaml.read_yaml_file("conf/application.yaml")
        profileName = commonConfig['application']['active']['profile']
        profileConfig = get_yaml.read_yaml_file("conf/application-" + profileName + ".yaml")
        config = {**langConfig}
        app.config.update(config)
        app.config['LANG'] = commonConfig['LANG']

        ##添加redis配置文件到flask App中
        app.config['REDIS_HOST'] = profileConfig['Redis']['HOST']
        app.config['REDIS_PORT'] = profileConfig['Redis']['PORT']
        app.config['REDIS_PASS'] = profileConfig['Redis']['PASSWORD']
        app.config['REDIS_DB'] = profileConfig['Redis']['DB']
        app.config['REDIS_EXPIRE'] = profileConfig['Redis']['EXPIRE_TIME']
        app.config['REDIS_TIMEOUT'] = profileConfig['Redis']['TIMEOUT']

        # 加载日志配置
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        loggingConfig = get_yaml.read_yaml_file("conf/logging.yaml")
        loggingConfig['handlers']['file']['filename'] = './logs/message.log'
        logging.config.dictConfig(loggingConfig)

        # 添加数据库配置文件到flask App中
        _path = os.path.join(kwargs['path'], 'conf')
        _database = profileConfig['DataSource']['NAME'] + '.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(_path, _database)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # 注册数据库连接
        db.app = app
        db.init_app(app)
        from models.EnvData import EnvData
        db.create_all()

        # 注册定时任务
        if commonConfig['Scheduler']['ENABLE']:
            app.config['SCHEDULER_API_ENABLED'] = True
            app.config['SCHEDULER_EXECUTORS'] = {
                'default': {'type': 'threadpool', 'max_workers': commonConfig['Scheduler']['THREADPOOL']}}
            app.config['SCHEDULER_JOB_DEFAULTS'] = {'coalesce': False,
                                                    'max_instances': commonConfig['Scheduler']['MAX_INSTANCES']}
            app.config['JOBS'] = []
            # from app.Air.CollectData import collect
            # app.config['JOBS'].append({'id': 'collect', 'func': collect, 'args': None,'trigger': 'interval', 'seconds': 60})
            scheduler_init(app)

        # 注册蓝图
        from api.router import router
        router.append(exception)
        register_api(app, router)

        return app
    except Exception as e:
        print(e)
        os._exit(1)