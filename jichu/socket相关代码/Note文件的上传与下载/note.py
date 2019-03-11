import os
import  struct
# filepath=r'G:\python视频\Python全栈9期（第一部分）：基础+模块+面向对象+网络编程\day32\day32\Note文件的上传与下载'
# filename = 'txt.py'
# file=os.path.join(filepath,filename)
# filesize = os.path.getsize(file)
# print(filesize)
# with open(file,'r') as f:
#     for line in f:
#         print(line.strip())

num=struct.pack('i',90900000)
print(num) #b' \x06k\x05'
print(type(num)) #<class 'bytes'>
ret=struct.unpack('i',num)[0]
print(ret) #90900000
print(type(ret)) #<class 'int'>
