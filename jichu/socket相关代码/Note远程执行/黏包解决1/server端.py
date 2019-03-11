##服务端发送命令给客户端 客户端接收命令以后执行
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
    #发送命令
    conn.send(cmd.encode('utf-8'))
    #接收数据的长度
    num=int(conn.recv(1024).decode('utf-8'))
    print(num)
    #告诉client接收到了长度，也防止客户端发送数据长度——》发送数据之间发生黏包，
    # 现在过程变成发送数据长度——》接收server端的反馈---->发送数据之间发生黏包，
    conn.send('I have receive your maessage length,please sned your data'.encode('utf-8'))
    #接收数据
    data=conn.recv(num).decode('utf-8')
    print(data)
    print(len(data))
conn.close()
sk.close()



