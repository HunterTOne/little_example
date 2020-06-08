'''
def set_func(func):
    def call_func():
        print('----这是权限验证1-----')
        print('----这是权限验证2------')
        func()
    return call_func

@set_func   #等价于test1 = set_func(test1)
def test1():
    print('-----test1------')

# test1 = set_func(test1)
# test1()
test1()
'''
#通用装饰器
def set_func(func):
    print('开始进行装饰')
    def call_func(*args,**kwargs):
        print('----这是权限验证1-----')
        print('----这是权限验证2------')
        return func(*args,**kwargs) #相当于传递了两个参数：1个元组，1个字典
    return call_func

@set_func   #等价于test1 = set_func(test1)
def test1(num,*args,**kwargs):
    print('-----test1------')
    print('----test1----',args)
    print('-----test1----',kwargs)
    return 'OK'

# test1 = set_func(test1)
# test1()
ret = test1(100)
print(ret)