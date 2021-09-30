# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 19:59
# @Author  : Jaywatson
# @File    : task_scheduler.py
# @Soft    : backend_flask

from flask import current_app
from libs.core import scheduler

class TaskScheduler():

    @classmethod
    def add_job(cls, jobid, func, args, **kwargs):
        '''
        添加任务
        :param jobid: 任务id
        :param func: 功能名称
        :param args: 功能参数
        :param kwargs: {
            trigger: 触发器
        }
        :return:
        '''
        job_def = dict(kwargs)
        job_def['id'] = jobid
        job_def['func'] = func
        job_def['args'] = args
        job_def = cls.fix_job_def(job_def)
        cls.remove_job(jobid)
        current_app.apscheduler.add_job(**job_def)

    @classmethod
    def remove_job(cls, jobid, jobstore=None):
        """删除任务"""
        try:
            current_app.apscheduler.remove_job(jobid, jobstore=jobstore)
        except:
            pass

    @classmethod
    def resume_job(cls, jobid, jobstore=None):
        """恢复任务"""
        current_app.apscheduler.resume_job(jobid, jobstore=jobstore)

    @classmethod
    def pause_job(cls, jobid, jobstore=None):
        """恢复任务"""
        current_app.apscheduler.pause_job(jobid, jobstore=jobstore)

    @staticmethod
    def fix_job_def(job_def):
        '''格式化任务'''
        if job_def.get('trigger') == 'date':
            job_def['run_date'] = job_def.get('run_date', None)
        elif job_def.get('trigger') == 'cron':  # quartz表达式
            quartzType = ['second','minute','hour','day','month','day_of_week','year']
            quartz = job_def['cron']
            del job_def['cron']
            for i in range(quartz):
                if quartz[i] == 'L':
                    job_def[quartzType[i]] = 'last'
                elif quartz[i] != '*' and quartz[i] != '?':
                    job_def[quartzType[i]] = quartz[i]
        elif job_def.get('trigger') == 'interval':
            interval = job_def['interval']
            del job_def['interval']
            for k,v in interval.items():
                job_def[k] = v
        return job_def
