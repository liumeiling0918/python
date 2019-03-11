import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
usr=input('>>>your name is:')
pwd=input('>>>your password is:')
sk.send(usr.encode('utf-8'))
sk.send(pwd.encode('utf-8'))
msg=sk.recv(1024).decode('utf-8')
print(msg)
