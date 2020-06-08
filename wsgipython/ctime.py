# coding:utf-8

import time

def application(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type','text/plain')
    ]
    #将这两个参数传给start_response函数
    start_response(status,headers)
    #
    return time.ctime()