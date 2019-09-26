"""
客户端
功能：根据用户输入，发送请求，得到结果
结构：
    一级界面 -->注册 登录 退出
    二级界面 -->查单词 历史记录 注销
"""
from  socket import *
from getpass import  getpass   #运行只能使用终端
import sys
import pymysql

#服务器地址
ADDR=('0.0.0.0',6060)
#功能函数都需要套接字，定义为全局变量
#搭建客户端网络
s = socket()
s.connect(ADDR)

#注册函数
def do_register():
    while True:
        name = input("User:")
        passwd= getpass()
        passwd_=getpass("Again:")
        #判断是否有空格
        if (' 'in name)or (' 'in passwd):
            print("不能包含空格")
            continue
        if passwd !=passwd_:
            print("两次密码不一致")
            continue

        msg="R %s %s"%(name,passwd)
        s.send(msg.encode())  #发送请求
        data=s.recv(128).decode()    #接受反馈
        if data=="OK":
            print("注册成功")
            log_in(name)
        else:
            print("注册失败")
        return

#登录
def do_log_in():
    while True:
        name=input("user:")
        passwd=getpass()
        msg = "L %s %s" % (name, passwd)
        s.send(msg.encode())  # 发送请求
        data = s.recv(128).decode()  # 接受反馈
        if data == "OK":
            print("登录成功")
            log_in(name)
        else:
            print("登录失败")
        return

def log_in(name):
    while True:
        print("""
        ===========Query===============
        1.查单词    2.历史记录      3.注销
        ===============================
        """)
        cmd=input("输入选项:")
        if cmd == '1':
            do_query(name)
        elif  cmd == '2':
            do_history(name)
        elif  cmd == '3':
            return
        else:
            print("请输入正确选项")
#查询单词
def do_query(name):
    while True:
        word=input("word:")
        if word =="##":  #结束查询
            break
        msg="I %s %s"%(name,word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        # if data=="OK":
        #     print(data)
        # else:
        #     print("没有该单词")
        print(data)

#历史记录
def do_history(name):
    msg="H %s"%name
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data=="OK":
        while True:
            data=s.recv(4096).decode()
            if data=="##":
                break
            print(data)
    else:
        print("无历史记录")












def main():
    while True:
        print("""
        =========Welcome===============
        1.注册       2.登录      3.退出
        ===============================
        """)
        cmd=input("输入选项:")
        if cmd == '1':
            do_register()
        elif  cmd == '2':
            do_log_in()
        elif  cmd == '3':
            s.send(b"Q")
            sys.exit("bye")
        else:
            print("请输入正确选项")

if __name__=="__main__":
    main()