import re



'''
def main():
    names = ['zhang','_zhang','8zhang','zhang2','a_zhang','zhang_9','zhang!','z#hang123']
    for name in names:
        ret = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$',name)
        if ret:
            print('变量名：%s 符合要求。。通过正则匹配出来的数据是：%s'%(name,ret.group()))
        else:
            print('变量名: %s 不符合要求。。。。'%name)

if __name__ == '__main__':
    main()
'''
'''
正则表达式163邮箱地址
'''

def main():
    email = input('请输入一个邮箱地址：')
    #如果需要某些字符的本意时，比如.  ?  等，用反斜杠\进行转义。
    ret = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$',email)
    if ret :
        print('邮箱地址%s符合要求,通过正则匹配出的数据是%s'%(email,ret.group()))
    else:
        print('邮箱地址%s不符合要求'%email)

if __name__ == '__main__':
    main()
'''
create table student(
    id int unsigned not null auto_increment primary key,
    name varchar(30), 
    age tinyint unsigned default 21,
    high decimal(5,2) ,
    sex enum ('男','女','中性') default'女',
    cls_id int unsigned
)charset = utf8;
'''








