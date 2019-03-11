#通过struct模块解决黏包问题
import struct
import socket
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.bind(ip_port)
sk.listen()
conn,addr=sk.accept()
while True:
    cmd=input('cmd:')
    if cmd=='q':
        print('over')
        break
    #发送命令给客户端
    conn.send(cmd.encode('utf-8'))
    #接收数据的长度
    num=conn.recv(4)
    num=struct.unpack('i',num)[0]
    msg=conn.recv(num).decode('utf-8')
    print(msg)
conn.close()
sk.close()



