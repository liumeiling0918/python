#客户端传输问价给服务端
#1.先发送报文头的长度
#2.发送报文头
#3.发送报文（服务端从报文头中读取报文长度）
import socket
import os
import json
import struct
ip_port=('127.0.0.1',8080)
buffersize=1024
sk=socket.socket()
sk.connect(ip_port)

#生成报文头
filepath='G:\python视频\Python全栈9期（第一部分）：基础+模块+面向对象+网络编程\day32'
filename='01 python fullstack s9day32 复习.mp4'
f=os.path.join(filepath,filename)
filesize=os.path.getsize(f)
head={'filepath':filepath,'filename':filename,'filesize':filesize}
#序列化 将字典转化成字符串
headstr=json.dumps(head)
#编码
headbyte=headstr.encode('utf-8')
#发送报头的长度
num=struct.pack('i',len(headbyte))
sk.send(num)
#发送报头
sk.send(headbyte)
#发送报文
with open(f,'rb') as f:
    while filesize:
        if filesize>=buffersize:
            content=f.read(buffersize)
            sk.send(content)
            filesize-=buffersize
        else:
            content=f.read(filesize)
            sk.send(content)
            filesize=0
            print('end')
            break
sk.close()




