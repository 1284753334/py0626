from datetime import datetime

from django.shortcuts import render,redirect,reverse
from resource.models import Resource,User
from django.shortcuts import HttpResponse
from django.db import transaction
from py1905.decorators import auth_sesson
from django.core.paginator import Paginator
from django_redis import get_redis_connection
import json
from django.core.serializers.json import DjangoJSONEncoder
import time
from django.views.decorators.cache import cache_page


def path(request,path):

    return render(request,f"{path}.html")


@cache_page(30)
@transaction.atomic
def index(request):
    """
    系统首页
    :param request:
    :return:
    """
    start =time.time()
    # 先判断缓存中是否有数据，有，则优先使用缓存中的数据，
    #  否则，再考虑 使用从数据库查询
    #redis = get_redis_connection()
    # print(redis)
    # if not redis.get()


    # 从数据库查询所有的资源
    data2= Resource.objects.order_by("-resourceTime")
    #实现分页显示
    # 将查询到的数据 放到分页对象中，并设置显示条数
    P = Paginator(data2, 3)

    # 获取当前要取第几页的数据
    page =  request.GET.get('page') if request.GET.get('page') else 1
    # 获取指定页面的数据
    data = P.get_page(page)
    print(data)
    print(type(data))
    print(data)

    # 获取用户头像
    # print(data2)
    # data2=[
    #     {"id":1,'resourceName':"python权威指南","resourceDesc":"这书很良心，不错","user":"张三","uploadTime":datetime.now(),"score":2},
    #     {"id": 2, 'resourceName': "jave权威指南", "resourceDesc": "这书很良心，不错", "user": "张三", "uploadTime": datetime.now(),
    #      "score": 0},
    #     {"id": 1, 'resourceName': "php权威指南", "resourceDesc": "这书很良心，不错", "user": "张三", "uploadTime": datetime.now(),
    #      "score": 2},
    # ]

    end = time.time()
    run  = end-start
    print("运行时间为：",run)
    return render(request,'index.html',{'data':data})


@transaction.atomic
def login(request):
    # 从页面获取参数
    username= request.POST.get("username")
    password = request.POST.get("password")
    print(username,password)
    # 从数据库查询参数
    user = User.objects.filter(username=username).first()
    print(user)
    # 假如查到了用户
    if not user:
        # return HttpResponse("用户名不正确")
        #  输入用户名或密码 错误，不显示  任何信息
        return render(request,"index.html",{"msg":"用户名不正确"})
    if password != user.password:
        # return HttpResponse("密码不正确")
        return render(request, "index.html", {"msg": "密码不正确"})

    # 存储用户登录 成功的标识、该标识存储在 session 会话中

    request.session['loginFlag'] = {"username":user.username,"id":user.id}

    print(request.session['loginFlag'])
    # 查看session有哪些方法
    # print(dir(request.session))
    # 查看对set_expiry的解释
    # flush  清空当前session
    # request.session.flush()
    # 清除过期的session
    request.session.clear_expired()
    # print(help(request.session.set_expiry))

    # 设置 session 过期时间
    request.session.set_expiry(60*30)


    #{"username":user.username,"id":user.id}
    #  信息 无误，页面有上传的资源信息
    return redirect(to=reverse("index" ))
    # 可以使用 args 添加参数
    #return redirect(to=reverse("index" ,args=["id":id]))


# 实现退出登录
@transaction.atomic
def exist(request):
    request.session.flush()
    return render(request,"index.html")

@auth_sesson
def get_photo(request):
    # 在session 中获取用户id 查询头像
    userId =request.session.get("loginFlag").get("id")
    # 根据用户id查询用户头像
    photo = User.objects.get(id = userId).photo

    #
    with photo.open() as f:
        content =  f.read()
    return HttpResponse(content)










