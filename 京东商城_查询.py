from pymysql import *


class JD(object):
    def __init__(self):
        # 创建connection链接
         self.conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='123456',charset='utf8')
        # 获得游标对象
         self.cursor= self.conn.cursor()

    def __del__(self):
        # 关闭对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_goods(self):
        '''显示所有商品'''
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_cates(self):
        #查询分类
        sql = 'select name  from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    def add_brands(self):
        item_name = input('请输入商品分类的名称：')
        sql = 'insert into goods_brands (name) value ("%s") '%item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input('请输入要查询的商品名称：')
        sql = 'select * from goods where name = "%s";'%find_name
        self.execute_sql(sql)

    def register(self):
        #请注册
        name = input('请输入你的用户名：')
        passwd = input('请输入你的密码：')
        address = input('请输入家庭地址：')
        tel = input('请输入你的电话号码：')
        sql = 'insert into customers (name,address,tel,passwd) value ("%s","%s","%s","%s")'%(name,address,tel,passwd)
        self.cursor.execute(sql)
        self.conn.commit()
        print('*****恭喜注册成功,请登陆*****')

    def login(self):
        #登陆功能
        name = input('请输入您的用户名：')
        passwd = input('请输入密码：')
        #从数据表中查出的相对应就是正确
        sql ="select passwd from customers where name='%s';"%name
        self.cursor.execute(sql)
        # 获取查询的结果\
        result = self.cursor.fetchone()
        #print(result)
         # 打印查询结果
        if passwd ==str(result[0]):
            print('登陆成功')
        else:
            print("密码错误，请重新输入")





    @staticmethod
    def printMenu():
        print('---------欢迎来到京东商城-------')
        print('****如果没有注册，请先登陆再注册****')
        print('1.查看的商品')
        print('2.查看的商品分类')
        print('3.查看的商品品牌的分类')
        print('4.添加商品的种类')
        print('5.根据名字查询商品')
        print('6.请先注册')
        print('7.欢迎登陆')
        return input('请输入对应的数字：')

    def run(self):
        #多个用户
        while True:
            num  = self.printMenu()
            if num =='1':
                #查询所有的商品
                self.show_all_goods()
            elif num=='2':
                #查询分类
                self.show_cates()
            elif num =='3':
                #查询品牌分类
                self.show_brands()
            elif num =='4':
                #添加商品种类
                self.add_brands()
            elif num == '5':
                #根据名字查询商品
                self.get_info_by_name()
            elif num =='6':
                #进行注册
                self.register()
            elif num=='7':
                #进行登陆
                self.login()
            else:
                print('请输入正确的数字')

def main():
    #1.创建一个京东商城对象
    jd = JD()
    #2.调用这个对象的run方法，让其运行
    jd.run()

if __name__ =='__main__':
    main()