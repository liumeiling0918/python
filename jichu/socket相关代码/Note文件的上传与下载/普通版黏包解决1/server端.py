#客户端传输文件给服务端
#1.接收报文头的长度
#2.接收报文头
#3.接收报文（从报文头中读取报文长度）
import socket
import struct
import json
ip_port=('127.0.0.1',8080)
buffersize=1024
sk=socket.socket()
sk.bind(ip_port)
sk.listen()
conn,addr=sk.accept()
#接收报头的长度
headlen=conn.recv(4)
headlen=struct.unpack('i',headlen)[0]
#按照报头的长度接收报头
head=conn.recv(headlen).decode('utf-8')
#反序列化
headDic=json.loads(head)
filesize=headDic['filesize']
filename=headDic['filename']
#接收报文
with open(filename,'wb') as f:
    while filesize:
        if filesize>=buffersize:
            content=conn.recv(buffersize)
            f.write(content)
            filesize=filesize-buffersize
        else:
            content=conn.recv(filesize)
            f.write(content)
            filesize=0
            print('end')
            break

conn.close()
sk.close()



