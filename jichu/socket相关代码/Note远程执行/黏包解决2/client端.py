import socket
import subprocess
import struct
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.connect(ip_port)
while True:
    #接收命令
    cmd=sk.recv(1024).decode('utf-8')
    #执行命令
    ret=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out=ret.stdout.read().decode('gbk')
    std_err=ret.stderr.read().decode('gbk')
    std_out='stdout is:'+std_out
    std_err='stderr is:'+std_err
    msg=(std_out+std_err).encode('utf-8')
    #计算要发送的数据的字节长度
    len_msg=len(msg)
    len_msg=struct.pack('i',len_msg)
    #发送长度给服务端
    sk.send(len_msg)
    #发送数据给服务端
    sk.send(msg)