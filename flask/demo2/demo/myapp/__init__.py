#coding=utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config,Config
from flask_pagedown import PageDown
from .admin import views as admin_views
from flask_admin import Admin,AdminIndexView
from flask_babelex import Babel
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op
from .models import db,login_manager,Whoosh

from .celery_email import flask_celery,mail
from .socket_msg import socketio
import flask_whooshalchemyplus



pagedown = PageDown()
bootstrap = Bootstrap()

moment = Moment()


babel=Babel()
admin = Admin(
    index_view=AdminIndexView(
    name=u'导航',
    template='admin/welcome.html',
    url='/welcome'  #http://127.0.0.1:5000/welcome
    )
)

admin.add_view(admin_views.MyView(name='新闻',endpoint='my'))
admin.add_view(admin_views.hello1(name='Hello 1', endpoint='test1', category='信息'))
admin.add_view(admin_views.hello2(name='Hello 2', endpoint='test2', category='信息'))
admin.add_view(admin_views.hello3(name='Hello 3', endpoint='test3', category='信息'))
path = op.join(op.dirname(__file__), 'static/img')
admin.add_view(FileAdmin(path, '/static/', name='文件',endpoint='file'))
admin.add_view(admin_views.MyV1(db.session, name=u'管理新闻'))

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
def create_app(config_name):
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .socket_io import socket_io as socket_io_blueprint
    app = Flask(__name__)
    app.config['BABEL_DEFAULT_LOCALE']='zh_CN'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    babel.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    socketio.init_app(app)
    flask_celery.conf.update(app.config)
    flask_whooshalchemyplus.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(socket_io_blueprint)

    return app


# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_pagedown import PageDown
# from celery import Celery
# from config import config, Config
#
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()
# pagedown = PageDown()
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
#
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
#
#
# def create_app(config_name):
#     myapp = Flask(__name__)
#     myapp.config.from_object(config[config_name])
#     config[config_name].init_app(myapp)
#
#     bootstrap.init_app(myapp)
#     mail.init_app(myapp)
#     moment.init_app(myapp)
#     db.init_app(myapp)
#     login_manager.init_app(myapp)
#     pagedown.init_app(myapp)
#     celery.conf.update(myapp.config)
#
#     if not myapp.debug and not myapp.testing and not myapp.config['SSL_DISABLE']:
#         from flask_sslify import SSLify
#         sslify = SSLify(myapp)
#
#     from .main import main as main_blueprint
#     myapp.register_blueprint(main_blueprint)
#
#     from .auth import auth as auth_blueprint
#     myapp.register_blueprint(auth_blueprint, url_prefix='/auth')
#
#
#     return myapp
