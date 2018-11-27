import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.bind(('127.0.0.1', 999))

for i in range(9994,10006):
    try:
        s.connect(('127.0.0.1', i))
        global j        
        j=i
    except:
        pass
# 接收欢迎消息:
print(j)
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
# 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()