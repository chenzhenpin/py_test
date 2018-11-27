#coding=utf-8
from flask.ext.mail import Message
from flask import current_app, render_template
from celery import Celery
from flask_mail import Mail
from config import config,Config
from threading import Thread
#windows上不支持celery4

flask_celery = Celery()
mail = Mail()
@flask_celery.task
def subn():
    return 'niac tome you'

@flask_celery.task(
    bind=True,
    igonre_result=True,
    default_retry_delay=300,
    max_retries=5)
def send_async_email(msg):
    mail.send(msg)


def send_email(to, subject, template, **kwargs):
    #获取app对象才能使用app.
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    send_async_email.delay(msg)

