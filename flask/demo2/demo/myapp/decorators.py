#coding=utf-8
from functools import wraps
from flask import abort
from flask.ext.login import current_user
from .models import Permission
#检查用户自定义权限的装饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(404)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)