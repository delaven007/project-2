"""
用于httpserver测试
"""
from socket import *
import json

s=socket()
s.bind(('0.0.0.0',8080))
s.listen(1)
c,addr=s.accept()
data=c.recv(4096).decode()
print(json.loads(data))

d={'status':'200','data':'hello world'}
data=json.dumps(d)

c.send(data.encode())
c.close()
s.close()