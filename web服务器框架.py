# coding:utf-8
'''
import time
#构建框架
class Application(object):

    def __init__(self,urls):
        self.urls = urls

    def __call__(self, env,start_response):
        path = env.get('PATH_INFO ')
        for url in

app = Application()
#构建一个服务器，接受app,当作函数调用，调用时也就是调用了call方法
http_server = HTTPServer(app)
app(env,start_response)


#做一个框架
def application(env, start_response):

    #路由地址   路径信息与函数
    urls = {
        ('/ctime',show_ctime)

    }
    status = '200 OK'
    headers = [
        ('Content-Type','text/plain')
    ]
    #将这两个参数传给start_response函数
    start_response(status,headers)
    #
    return time.ctime()
'''