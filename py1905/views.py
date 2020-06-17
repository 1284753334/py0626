from datetime import datetime

from django.shortcuts import render
from resource.models import Resource


def path(request,path):

    return render(request,f"{path}.html")


def index(request):
    """
    系统首页
    :param request:
    :return:
    """
    # 从数据库查询所有的资源
    data2= Resource.objects.all()
    print(data2)
    # data2=[
    #     {"id":1,'resourceName':"python权威指南","resourceDesc":"这书很良心，不错","user":"张三","uploadTime":datetime.now(),"score":2},
    #     {"id": 2, 'resourceName': "jave权威指南", "resourceDesc": "这书很良心，不错", "user": "张三", "uploadTime": datetime.now(),
    #      "score": 0},
    #     {"id": 1, 'resourceName': "php权威指南", "resourceDesc": "这书很良心，不错", "user": "张三", "uploadTime": datetime.now(),
    #      "score": 2},
    # ]
    return render(request,'index.html',{'data':data2})