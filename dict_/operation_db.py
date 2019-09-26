"""
dict 数据库管理
功能：提供服务端所有数据库操作
"""
import pymysql
import hashlib

SALT="#%AID1904_"  #盐

class Database:
    def __init__(self,host='localhost',port=3306,user='root',passwd='123456',charset='utf8',database ='dict'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.charset=charset
        self.database=database
        self.connect_db()     #连接数据库


    def connect_db(self):
        self.db=pymysql.connect(host=self.host,
                                port=self.port,
                                user=self.user,
                                passwd=self.passwd,
                                charset=self.charset,
                                database=self.database)
    #创建游标
    def create_cursor(self):
        self.cur=self.db.cursor()

    def close(self):
        self.db.close()


    #注册操作
    def register(self,name,passwd):
        sql="select * from user where name='%s'"%name
        self.cur.execute(sql)
        r=self.cur.fetchone()    #如果有查询结果，name存在
        if r:
            return False


        #密码加密处理
        hash = hashlib.md5((name+SALT).encode())
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 提取加密后的密码

        #插入数据库
        sql="insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False
    #登录
    def log_in(self,name,passwd):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 提取加密后的密码
        sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
        self.cur.execute(sql)
        r=self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def query(self,word):
        sql = "select mean from words where word ='%s'"%word
        self.cur.execute(sql)
        r=self.cur.fetchone()
        if r:
            return r[0]

    def insert_history(self, name, word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def history(self,name):
        sql="select name,word,time from hist where name='%s' order by time desc limit 10"%name

        self.cur.execute(sql)
        return self.cur.fetchall()

















    #
    # def history(self):
    #     sql = "select * from student where gender='m'"
    #     self.cur.execute(sql)  # 执行查询后cur会拥有查询结果
    #
    #     # 获取一个查询结果
    #     # one_row =cur.fetchone()
    #     # print(one_row)
    #     #
    #     #
    #     # #获取多个查询结果
    #     # many_row=cur.fetchmany(100)
    #     # print(many_row)
    #
    #     # 获取全部查询结果
    #     all_row = self.cur.fetchall()
    #     print(all_row)
    #
    #     # 关闭数据库
    #     self.cur.close()
    #     self.db.close()