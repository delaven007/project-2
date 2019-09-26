# import getpass  #隐藏输入
# import hashlib  #转换加密
#
# #输入隐藏
# pwd=getpass.getpass("passwd:")
#
# # hash=hashlib.sha1()         #生成对象
#
# #算法加盐 (#$awv3_)
# hash=hashlib.sha1("*#%^&*asdf54".encode())
#
# hash.update(pwd.encode())     #算法加密
# pwd=hash.hexdigest()        #提取加密后的密码
# print(pwd)

import  getpass
import hashlib
pwd=getpass.getpass('passwd:')
# hash=hashlib.md5()
hash=hashlib.md5('#%%^&sd352'.encode())
hash.updata(pwd.encode())
pwd=hash.hexdigest()
print(pwd)