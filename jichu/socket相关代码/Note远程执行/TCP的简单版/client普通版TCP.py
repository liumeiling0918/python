#客户端接收命令以后，执行命令
import socket
import subprocess
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.connect(ip_port)
while True:
    com=sk.recv(1024).decode('utf-8')
    ret=subprocess.Popen(com,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #管道中的内容只能读一次，类似于队列中的出队操作
    read_out=ret.stdout.read().decode('gbk') #byte类型 gbk编码
    read_err=ret.stderr.read().decode('gbk') #byte类型 gbk编码
    sk.send(('stdout is:'+read_out).encode('utf-8'))
    sk.send(('stderr is:'+read_err).encode('utf-8'))

sk.close()

