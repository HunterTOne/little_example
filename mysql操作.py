from pymysql import *


def main():
    # 创建Connection连接
    #host表明要连接谁    127.0.0.1  指向本地，链接本地服务器
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='123456', charset='utf8')
    # 获得Cursor对象  cursor()方法给一个返回值就是游标对象
    cs1 = conn.cursor()

    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    #good = cs1.execute('select * from goods;')
    # count = cs1.execute('insert into goods_cates(name) values("ipad")')
    # # 打印受影响的行数
    # print(count)
    #
    # count = cs1.execute('insert into goods_cates(name) values("学习机")')
    # print(count)
    #查询一条数据
    count = cs1.execute('select id,name from goods where id>=4')
    #打印受影响的行数
    print('查询到%d的行数：'%count)

    for i in range(count):
        #获取查询的结果
        result = cs1.fetchone()
        #打印查询结果
        print(result )

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()
    #关闭游标对象
    cs1.close()
    #关闭connection对象
    conn.close()

if __name__ == '__main__':
    main()









