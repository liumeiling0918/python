import socket
import hmac
import struct
key=b'egg'
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.connect(ip_port)
msg=sk.recv(1024)
#对密钥和信息进行加密
h=hmac.new(key,msg)
ret=h.hexdigest() #str类型
#发送密文的长度
num=struct.pack('i',len(ret)) #byte类型
sk.send(num)
#发送密文
sk.send(ret.encode('utf-8'))

