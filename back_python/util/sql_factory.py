# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:37
# @Author  : Jaywatson
# @File    : SQLFactory.py
# @Soft    : backend_flask
import logging
from libs.core import db

logger = logging.getLogger("libs")

class BaseSql:

    __model__ = None

    def __init__(self, object = None):
        self.__model__ = object

    '''插入'''
    def insert(self, args):
        for data in args:
            model = self.__model__()
            for k, v in data.items():
                setattr(model, k, v)
            db.session.add(model)
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            return False

    '''删除'''
    def delete(self,key):
        model = self._get(key)
        if model:
            try:
                db.session.delete(model)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                logger.error(e)
                return False

    '''更新'''
    def update(self,key,args):
        model = self.get(key)
        if model:
            for k, v in args.items():
                setattr(model, k, v)
            db.session.add(model)
            try:
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                logger.error(e)
                return False

    '''查询'''
    def select(self,args):
        datas = self.__model__.query.filter(*args).all()
        return self.__parse_data(datas)

    '''分页查询'''
    def select_by_page(self, args):
        print(4)

    '''根据主键ID获取数据'''
    def get(self, key):
        return self.__model__.query.get(key)

    '''直接执行sql'''
    def execute_sql(self, sql, conditions=[], page=-1, limit=-1):
        parms = {}
        if len(conditions) >0:
            if 'where' not in sql:
                sql = sql + " where 1=1"
            for condition in conditions:
                sql = sql + " " + condition['logic']
                sql = sql + " " + condition['sql']
                parms[condition['key']] = condition['value']
        if page != -1 and limit != -1:
            offset_size = (page - 1) * limit
            sql = sql + " limit :limit_size offset :offset_size"
            parms.update({
                "limit_size": limit,
                "offset_size": offset_size
            })
        results= db.session.execute(sql, parms)
        return [dict(zip(result.keys(), result)) for result in results]

    '''结果格式化'''
    def __parse_data(self,datas):
        if isinstance(datas, (list, tuple)):
            datas = list(map(lambda x: {prop.key: getattr(x, prop.key) for prop in self.__model__.__mapper__.iterate_properties},datas))
        else:
            datas = {prop.key: getattr(datas, prop.key) for prop in self.__model__.__mapper__.iterate_properties}
        return datas