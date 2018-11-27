#coding=utf-8
from flask.ext.admin import  BaseView, expose
from flask import url_for
from flask.ext.login import current_user
from flask_admin.contrib.sqla import ModelView
from ..models import Post



class MyView(BaseView):
    #改函数返回真才能访问该导航
    def is_accessible(self):
        return current_user.is_authenticated  #用户登录返回真。
    # http://127.0.0.1:5000/welcome/my/
    @expose('/')
    def index(self):
        url = url_for('.view')
        return self.render('admin/home.html',url=url)
    #http://127.0.0.1:5000/welcome/my/view
    @expose('/view')
    def view(self):
        return self.render('admin/view.html')

class hello1(BaseView):
    # http://127.0.0.1:5000/welcome/test1/
    @expose('/')
    def index(self):
        return self.render('admin/hello1.html')
class hello2(BaseView):
    # http://127.0.0.1:5000/welcome/test2/
    @expose('/')
    def index(self):
        return self.render('admin/hello2.html')
class hello3(BaseView):
    # http://127.0.0.1:5000/welcome/test3/
    @expose('/')
    def index(self):
        url = url_for('my.view') #MyView.view函数
        return self.render('admin/hello3.html',url=url)





class UserView(BaseView):
    #改函数返回真才能访问该导航
    def is_accessible(self):
        return current_user.is_authenticated  #用户登录返回真。
    # http://127.0.0.1:5000/welcome/my/
    @expose('/')
    def index(self):
        url = url_for('.view')
        return self.render('admin/home.html',url=url)
    #http://127.0.0.1:5000/welcome/my/view
    @expose('/view')
    def view(self):
        return self.render('admin/view.html')

class MyV1(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated :
            return True
        return False
    can_create = False

    column_labels = {
        'id':u'序号',
        'body' : u'文章',
        'timestamp':u'发布时间',
        'author_id':u'作者id'
    }
    column_list = ('id', 'body','timestamp','author_id')
    def __init__(self, session, **kwargs):
        super(MyV1, self).__init__(Post,session, **kwargs)
