#给服务端发送客户端数据字节形式的大小
#注意：不能发送字符串形式的大小，因为字符串转换成字符byte以后,大小不一定相等
import socket
import subprocess
ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.connect(ip_port)
while True:
    #接收server端的命令
    cmd=sk.recv(1024).decode('utf-8')
    #执行server端的命令
    ret=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # 管道中的内容只能读一次，类似于队列中的出队操作
    std_out=ret.stdout.read().decode('gbk')
    std_err=ret.stderr.read().decode('gbk')
    std_out='stdout is:'+std_out
    std_err='stderr is:'+std_err
    msg=(std_out+std_err).encode('utf-8')
    #发送数据的长度
    sk.send(str(len(msg)).encode('utf-8'))
    #接收服务端的反馈
    re=sk.recv(1024).decode('utf-8')
    print(re)
    #发送数据
    sk.send(msg)

sk.close()

