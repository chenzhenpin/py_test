# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail, Message
from threading import Thread
import os

app = Flask(__name__)

# Flask-Mail 使用标准的 Flask 配置 API 进行配置，下面是一些常用的配置项：

# | 配置项 | 说明 |
# | --- | --- |
# | MAIL_SERVER  | 邮件服务器地址，默认为 localhost |
# | MAIL_PORT | 邮件服务器端口，默认为 25 |
# | MAIL_USE_TLS | 是否启用传输层安全 (Transport Layer Security, TLS)协议，默认为 False |
# | MAIL_USE_SSL | 是否启用安全套接层 (Secure Sockets Layer, SSL)协议，默认为 False |
# | MAIL_DEBUG | 是否开启 DEBUG，默认为 app.debug |
# | MAIL_USERNAME | 邮件服务器用户名，默认为 None |
# | MAIL_PASSWORD | 邮件服务器密码，默认为 None |
# | MAIL_DEFAULT_SENDER | 邮件发件人，默认为 None，也可在 Message 对象里指定 |
# | MAIL_MAX_EMAILS | 邮件批量发送个数上限，默认为 None |
# | MAIL_SUPPRESS_SEND | 默认为 app.testing，如果为 True，则不会真的发送邮件，供测试用 |
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  'chenzhenpingz@163.com'
app.config['MAIL_PASSWORD'] =  '74745656q'
app.config['MAIL_USE_TLS'] =  True   #qq只接受此连接方式


mail = Mail(app)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
		

@app.route('/sync')
def send_email():
    msg = Message('测试邮件', sender='chenzhenpingz@163.com', recipients=['1940497838@qq.com','1595347682@qq.com'])
    msg.html = '发送带附近的邮件'
    with app.open_resource(r"C:\Users\chenzhen\Desktop\flask\study\demo\w.jpg") as fp:   #添加附件
        msg.attach("photo.jpg", "image/jpeg", fp.read())
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return 'send successfully ,ok'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)