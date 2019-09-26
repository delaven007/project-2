"""
server主程序
"""
from socket import *
from threading import Thread
from config import *
import re
import json

ADDR=(host,port)

def connect_frame(env):
    s=socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
    data=json.dumps(env)
    s.send(data.encode())
    data=s.recv(1024*1024).decode()
    return json.loads(data)
