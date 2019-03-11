import hashlib
import hmac

#使用hashlib对密码加密
md5=hashlib.md5()
md5.update(b'12345')
ret=md5.hexdigest()
print(type(ret)) #str


#使用hmac对密码加密
h=hmac.new(b'key',b'123456')
ret1=h.hexdigest()
print(type(ret1))  #str

#使用hashlib验证密码的合法性
#用户hello 密码123456
#用户hello1 密码12345
usr=input('username:')
pwd=input('pwd:')
with open('info.py','r') as  f:
    for line in f:
        str=line.split('|')
        infousr=str[0]
        infopwd=str[1].strip()
        #str[0]为用户名 str[1]为密文存储的密码
        #在系统内部找到该用户：
        if infousr==usr:
            #对输入的密码进行摘要，并与系统内部存储的密码相比较
            md5=hashlib.md5()
            md5.update(bytes(pwd,encoding='utf-8'))
            pwd=md5.hexdigest()
            if infopwd==pwd:
                print('login sucess')
                break
            else:
                print('incorrect pwd')
                break




