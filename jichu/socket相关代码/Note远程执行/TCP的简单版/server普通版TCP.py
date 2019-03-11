#服务端发送命令给客户端 客户端接收命令以后执行
import socket
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.bind(ip_port)
sk.listen()
conn,addr=sk.accept()
while True:
    cmd=input('>>>')
    if cmd=='q':
        print('over')
        break
    conn.send(cmd.encode('utf-8'))
    msg = conn.recv(1024).decode('utf-8')
    print(msg)

conn.close()
sk.close()


