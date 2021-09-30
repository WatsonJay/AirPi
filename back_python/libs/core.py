# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 10:05
# @Author  : Jaywatson
# @File    : core.py
# @Soft    : back_python
import atexit
import platform
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, Blueprint
import redis

db = SQLAlchemy()
scheduler = APScheduler()

'''redis数据库操作'''
class RedisMethod(object):
    '''获取配置'''

    @staticmethod
    def _get_config():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        password = current_app.config['REDIS_PASS']
        db = current_app.config['REDIS_DB']
        timeOut = current_app.config['REDIS_TIMEOUT']
        redis_config = redis.StrictRedis(host= host, port= port, db= db, password= password,socket_connect_timeout= timeOut, socket_timeout=timeOut)
        return redis_config

    '''写入键值对'''

    @classmethod
    def write(cls, key, value, expire=None):
        redis_config = cls._get_config()
        if expire:
            expire_in_seconds = expire
            redis_config.set(key, value, ex=expire_in_seconds)
        else:
            redis_config.set(key, value)

    '''读取键值对'''

    @classmethod
    def read(cls, key):
        redis_config = cls._get_config()
        value = redis_config.get(key)
        return value.decode('utf-8') if value else ''

    '''写入hash表'''

    @classmethod
    def hset(cls, name, key, value):
        redis_config = cls._get_config()
        redis_config.hset(name, key, value)

    '''读取指定hash表的所有给定字段的值'''

    @classmethod
    def hmset(cls, key, *value):
        redis_config = cls._get_config()
        value = redis_config.hmset(key, *value)
        return value

    '''读取指定hash表的键值'''

    @classmethod
    def hget(cls, name, key):
        redis_config = cls._get_config()
        value = redis_config.hget(name, key)
        return value.decode('utf-8') if value else value

    '''获取指定hash表所有的值'''

    @classmethod
    def hgetall(cls, name):
        redis_config = cls._get_config()
        return redis_config.hgetall(name)

    '''删除一个或者多个'''

    @classmethod
    def delete(cls, *names):
        redis_config = cls._get_config()
        redis_config.delete(*names)

    '''删除指定hash表的键值'''

    @classmethod
    def hdel(cls, name, key):
        redis_config = cls._get_config()
        redis_config.hdel(name, key)

    '''设置过期时间'''

    @classmethod
    def expire(cls, name, expire=None):
        if expire:
            expire_in_seconds = expire
            redis_config = cls._get_config()
            redis_config.expire(name, expire_in_seconds)


'''注册蓝图'''
def register_api(app, routers):
    for router in routers:
        if isinstance(router, Blueprint):
            app.register_blueprint(router)
        elif isinstance(router, dict):
            try:
                for key, value in router.items():
                    endpoint = key.__name__
                    view_func = key.as_view(endpoint)
                    url = value
                    if 'GET' in router.__methods__:
                        app.add_url_rule(url, defaults={'key': None}, view_func=view_func, methods=['GET', ])
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['GET', ])
                    if 'POST' in router.__methods__:
                        app.add_url_rule(url, view_func=view_func, methods=['POST', ])
                    if 'PUT' in router.__methods__:
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['PUT', ])
                    if 'DELETE' in router.__methods__:
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['DELETE', ])
            except Exception as e:
                raise ValueError(e)


'''任务调度注册'''
def scheduler_init(app):
    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('--------Scheduler Started--------')
        except Exception as e:
            app.logger.error(e)

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('--------Scheduler Started--------')
        except Exception as e:
            app.logger.error(e)

        def _unlock():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass

        atexit.register(_unlock)