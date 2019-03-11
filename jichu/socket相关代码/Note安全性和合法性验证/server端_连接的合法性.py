#验证客户端连接的合法性
#1.服务端,客户端互相约定密钥
#2.服务端给客户端发送要加密的信息
#3.服务端，客户端分别对密钥和信息加密
#4.比较加密后的内容是否相同
import socket
import hmac
import struct
key=b'egg'
#验证合法性
def iscorrect(conn):
    msg='hello'
    #发送要加密的信息
    conn.send(msg.encode('utf-8'))
    #接收客户端加密后的内容的长度
    vf_len=conn.recv(4)
    vf_len=struct.unpack('i',vf_len)[0] #int型
    # 接收客户端加密后的内容
    vf_client=conn.recv(vf_len).decode('utf-8')
    #获取server端加密后的内容
    h=hmac.new(key,msg.encode('utf-8'))
    vf_server=h.hexdigest()
    return hmac.compare_digest(vf_server,vf_client)


ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.bind(ip_port)
sk.listen()
conn,addr=sk.accept()
#验证连接的合法性
if iscorrect(conn):
    print('合法')
else:
    print('不合法')
conn.close()
sk.close()
