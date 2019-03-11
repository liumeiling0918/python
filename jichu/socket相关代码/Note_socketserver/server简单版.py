#socketserver 简单版
#实现多个用户同时登录
import socketserver
class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            usr=self.request.recv(1024).decode('utf-8')
            pwd=self.request.recv(1024).decode('utf-8')
            print('username is:',usr)
            print('password is',pwd)
            msg=input('>>>')
            self.request.send(msg.encode('utf-8'))

if __name__=='__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),myserver)
    server.serve_forever()
