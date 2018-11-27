#coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))





class Config:
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'chenzhenpingz@163.com'
    FLASKY_POSTS_PER_PAGE=8 #配置查询文章分页的每页的额记录数
    FLASKY_COMMENTS_PER_PAGE=10 #配置查询评论分页的每页的额记录数
    SECRET_KEY = 'nice to me you'
    FLASKY_FOLLOWERS_PER_PAGE=10
    MAX_SEARCH_RESULTS = 50 #Whoosh 返回数据的最多条数
    #celery配置
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    #CELERY_TASK_SERIALIZER = 'json'# pickle
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    @staticmethod
    #@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME =  os.environ.get('MAIL_USERNAME') or 'chenzhenpingz@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '74745656q'
    FLASKY_ADMIN='1940497838@qq.com'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                                'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                                'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                'sqlite:///' + os.path.join(basedir, 'data.sqlite')
config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}