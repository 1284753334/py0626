
# 定义一个装饰器  作用 验证用户 是否登录
from django.shortcuts import redirect

def auth_sesson(func):
    '''
    fun 指 要装饰的函数 对象
    :param func:
    :return:
    '''
    def check_session(request,*args,**kwargs):
        # 1. 获取session ,判断 sesson 有没有 标识符
        dicts = request.session.get("loginFlag")
        if not dicts:
            return redirect(to="index.html")
        # 发现用户登录，重置session 时间
        request.session.set_expiry(60*30)

        # 清除过期的session
        request.session.clear_expired()

        # 如果用户登录 、则执行对应的处理方法
        return  func(request,*args,**kwargs)
    return check_session
