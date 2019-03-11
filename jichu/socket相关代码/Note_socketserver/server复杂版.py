#实现多个用户同时登录，并且用户密码的正确性
import  socketserver
import hashlib
class Userserver(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            #接收客户端发送的用户名和密码
            usr=self.request.recv(1024).decode('utf-8')
            pwd=self.request.recv(1024).decode('utf-8')
            #验证用户名和密码的合法性
            with open('info.py','r') as f:
                for line in f:
                    str=line.split('|')
                    if usr==str[0]:
                        str[1]=str[1].strip()
                        #对收到的密码进行摘要算法
                        h=hashlib.md5()
                        h.update(bytes(pwd,encoding='utf-8'))
                        ret=h.hexdigest()
                        if ret==str[1]:
                            print('login sucess')
                            self.request.send(b'login sucess')
                            break
                        else:
                            print('login fail')
                            self.request.send(b'login fail')
                            break








if __name__=='__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),Userserver)
    server.serve_forever()
