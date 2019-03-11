import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
usr=input('>>>please input your name')
pwd=input('>>>please input your password')
sk.send(usr.encode('utf-8'))
sk.send(pwd.encode('utf-8'))
msg=sk.recv(1024).decode('utf-8')
print(msg)
