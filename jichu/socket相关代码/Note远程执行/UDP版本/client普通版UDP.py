import socket
import subprocess
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.sendto(b'hello,pelase send your command',('127.0.0.1',8080))
while True:
    cmd=sk.recvfrom(1024)[0].decode('utf-8')
    ret=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #管道中的内容只能读一次，类似于队列中的出队操作
    std_out=ret.stdout.read().decode('gbk')
    std_err=ret.stderr.read().decode('gbk')
    sk.sendto(std_out.encode('utf-8'),('127.0.0.1',8080))
    sk.sendto(std_err.encode('utf-8'),('127.0.0.1',8080))
sk.close()
