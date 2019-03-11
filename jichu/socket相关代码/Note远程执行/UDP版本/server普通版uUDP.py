#服务端发送命令给客户端 客户端接收命令以后执行
import socket
ip_port=('127.0.0.1',8080)
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(ip_port)
msg,addr=sk.recvfrom(1024) #首先接收客户端信息，为了获取地址
print(msg)
while True:
    cmd=input('>>>')
    if cmd=='q':
        print('over')
        break
    sk.sendto(cmd.encode('utf-8'),addr)#发送命令
    re=sk.recvfrom(1024)[0].decode('utf-8')#接收命令执行结果
    print(re)
sk.close()

