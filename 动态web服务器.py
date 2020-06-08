# coding:utf-8
import sys
import re
from socket import *
from multiprocessing import Process


#用户请求时会有一个根路径，目录时固定的，不会变，所以是常量，所有字母必须大写
#设置静态文件根目录
HTML_ROOT_DIR ='./html'

WSGI_PYTHON_DIR = './wsgipython'


class HTTPServer(object):
    ''''''
    def __init__(self):
        # AF_INET是一个常量,对应一个具体的值
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 改一下socket级别对应的参数，重用地址，使端口号正常使用
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)



    def start(self):
        self.server_socket.listen(128)#在__init__函数中也行
        while True:
            # 开始等待客户端的连接,能够接受多个用户去连接，用多进程
            # 一直接受用户的连接
            client_socket, client_address = self.server_socket.accept()
            # 收到用户请求时，打印IP地址和端口
            # print('[%s,%S]用户连接上了'%(client_address[0],client_address[1]))
            print('[%s,%s]用户连接上了' % client_address)
            # print("[%s, %s]用户连接上了" % client_address)
            # 用进程的方式处理用户请求,新建进程的实例
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))  # 接受元组
            # 开启进程
            handle_client_process.start()
            # 子进程已经拿到了client_socket,所以关闭该client_socket
            client_socket.close()

    def start_response(self,status,headers):
        '''
        #自己服务器的响应头
        server_headers = [
            ('Server','My Server')
        ]
        #需要将headers和server_headers糅合到一起
        server_headers + headers
        '''
        '''
        status = '200 OK'
        headers = [
        ('Content-Type','text/plain')
    ]
    start.response(status,headers)
        '''
        response_headers ='HTTP/1.1 ' + status +'\r\n'
        for header in headers:
            response_headers +='%s: %s\r\n' % header
        self.response_headers = response_headers

    def handle_client(self,client_socket):
        # 函数描述文档
        '''获取客户端请求数据'''
        '''开启一个进程后，说明一个用户已经发送请求过来，已经accept
        三次握手已经成功了，客户端可以发送数据过来了，要接受用户数据
        '''
        request_data = client_socket.recv(1024)
        print('request data:', request_data)  # 打印请求的数据报文
        # 解析这个字符串,按照换行一行一行截取成列表
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        # 解析请求报文
        # 起始行是第一个元素，第一行是'GET / HTTP/1.1'
        request_start_line = request_lines[0]
        # 字符串的提取，将根路径提取出来，正则表达式做,group提取第一个括号里的东西
        # 提取用户请求的文件名   file_name就是/ctime
        file_name = re.match(r'\w+ +(/[^ ]*) ', request_start_line.decode('utf-8')).group(1)
        #method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        # 判断是否以.py结尾     '/time.py'
        if file_name.endswith('.py'):
            # 执行py文件,  将模块名进行相应的切片
            m = __import__(file_name[1:-3])#将包导入进来，有个返回值,是个模块
            env = {}
            #response_body接受了返回值time.ctime()
            response_body = m.application(env,self.start_response)
            response = self.response_headers + '\r\n'+ response_body
        else:
            # 默认主页，判断时通常反过来写，不可变、常量写到左边，，变量写道右边
            if '/' == file_name:
                file_name = '/index.html'
            try:
                # 打开这个文件，把内容读出来，然后返回回去
                file = open(HTML_ROOT_DIR + file_name, 'rb')  # 如果有图片，所以二进制
            except IOError:
                response_start_line = 'HTTP/1.1 404 Not Found\r\n'
                response_headers = 'Server:My server\r\n'
                response_body = '没有找到对应的文件'
            else:
                file_data = file.read()
                file.close()  # 读完之后可以关闭

                # 构造响应数据，是一个响应，有格式要求，有起始行，header，响应体
                response_start_line = 'HTTP/1.1 200 OK\r\n'
                response_headers = 'Server:My server\r\n'
                # 读文件后进行解码,\r\n代表换行符
                response_body = file_data.decode('utf-8')

             # 形成一个整体，组合响应体
            response = response_start_line + response_headers + '\r\n' + response_body
            print('response data:', response)
        # 响应有了可以往回发送了
        # 返回指定的报文，向客户端返回响应数据
        # 将response字符串转成字节，编码格式
        client_socket.send(bytes(response, 'utf-8'))
        # 发送完之后，可以关闭，代表一次请求结束
        client_socket.close()

    def bind(self,port):
        self.server_socket.bind(('', port))

def main():
    sys.path.insert(1,WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    # http_server.set_port
    #对象,开启服务器
    http_server.bind(8000)
    http_server.start()


if __name__=='__main__':
   main()



