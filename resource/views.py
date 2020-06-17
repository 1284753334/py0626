from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Q
from .models import Resource
from datetime import datetime
from .models import User
from hashlib import md5
from django.db import connection
from django.db import transaction
from django.views.decorators.http import *

from django.http.response import JsonResponse


# Create your views here.
def upload(request):
    """
    完成文件上传
    :param request:
    :return:
    """
    # 获取页面传过来的参数
    data= request.POST

    # 2.创建一个模型对象,用来存储数据
    res=Resource(
        resourceName= data.get("resourceName"),
        resourceType=data.get("resourceType"),
        resourceTime=datetime.now(),
        resourceSize=100,
        resource =data.get("resource"),
        Socre=data.get("Score"),
        keywords=data.get("keywords"),
        resourceDesc=data.get("resourceDesc"),
    )
    res.save()

    # 测试成功，页面跳转到首页

    return redirect(to ="/")
@require_GET
@transaction.atomic
def test(request):
    # 删除表中所有数据
    # User.objects.all().delete()

    # user= User.objects.create(username="张三",password='123')
    # user.delete()
    #
    # user.delete()
    # # get 返回一个对象
    #User.objects.get(id=3).delete()

    # 查询
    # user =User.objects.exclude(id=3)
    # print(User.objects.get(username="张三"))

    # in 查询
    # user = User.objects.filter(id__in=[4,7])
    # print(user)

    # 区间查询
    # user = User.objects.filter(Q(id=5)| Q(password= "123"))
    # print(user)
    # 排序
    # user = User.objects.filter(Q(id="5")|Q(password="123")).order_by("-id")

   # Queryset=User.objects.filter(id= "5")
    # print('===:',Queryset)
    # print(Queryset)
    # Queryset2 = User.objects.filter(id="6")
    # print('*********')
    # print(Queryset2,Queryset2)
    # User.objects.create(username='李四',password="123456")


    from django.db.models.aggregates import Count
    # 根据名字分组、并获取每一组的个数
    # s = User.objects.aggregate (t=Count("username"))
    # print(s)

    # 分组
    # t=User.objects.annotate(Count('username'))
    #     # print(t)

    # 指定查询的列
    # y=User.objects.all().values("id",'username')
    # print(y)

    # 测试一对多的数据
    '''
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    tel = models.CharField(max_length=11)
    Email= models.EmailField()

    sex =models.CharField(choices=sex_types,max_length=2)
    birth=models.DateField()


    '''
    # password='123'
    # password =md5(password.encode()).hexdigest()
    # user=User.objects.create(
    #     username="lisi",
    #     password =password,
    #     tel='13690569078',
    #     Email="12445@169.com",
    #     sex ='1',
    #     birth=datetime.now()
    # )
    #
    # # user=User.objects.get(id=1)
    # res=Resource(
    #         resourceName="测试",
    #
    #         resourceType="1",
    #         keywords="sdd,fgfg,d,dg",
    #
    #         Socre = "2",
    #
    #         resourceDesc = "asfdsgfg",
    #         resourceTime = datetime.now(),
    #
    #         resourceSize = 1000,
    #
    #        # 资源，FileField对应的数据库字段也是一个字符串
    #        resource = "bg.jpg",
    #          user =user.username
    # )
    # res.save()
    # 通过用户查找资源  失败
    # user = User.objects.get(id=1)
    # print(user)
    # print(user.resource_set)

    # 通过资源查找用户
    # res=Resource.objects.get(id=1)
    # print(res)
    # print(res.user)


# django 原生态操作语句
#     users = User.objects.raw("select * from t_resource")
#     print(users.iterator())
#     generate=users.iterator()
#     user  = next(generate)
#     print(user.password,user.username)
    # 支持 增删改查 的操作
    # with connection.cursor() as cursor:
    #     cursor.execute("select * from t_user t left join t_resource f on t.id=f.user_id where t.id=%s ",params=(1,) )
    #     t =cursor.description
    #     print(t)
    #     s = cursor.fetchall()
    #     print(s)
    #
    #     # cols=[]
        # for i in t:
        #     cols.append(i[0])
        #
        # _data = []
        # for x in s:
        #     _data.append(dict(zip(cols,x)))
        # print(_data)

        # 基于上述代码的改进

    #     cols=[i[0] for i in t]
    #     data=[dict(zip(cols,x))for x in s]
    #
    #     print(data)
    #
    # print(connection)
    # with connection.cursor() as cursor:
    #     cursor.execute("delete from t_resource where id= %s",params=(1,) )
    #     s =3
    #     t =s/0



    return  render(request,"test.html")
@require_POST
def test(request):
    return HttpResponse("post")


def check(request):
    """
    校验资源名是否可用
    :param request:
    :return:
    """
    #1. 接受页面参数
    name = request.GET.get("name")
    #2. 根据模型参数数据
    resource= Resource.objects.filter(resourceName=name)
    if resource:
        #return HttpResponse(Callback + '{"msg":"资源名已存在","status":False}')
        res= JsonResponse({"msg":"资源名已存在","status":0})
        res.setdefault("Access_Control-Allow-Origin","*")
        return res


    #return HttpResponse(Callback + '{"msg": "资源名可以使用", "status": True}')
    res = JsonResponse({"msg": "资源名不存在", "status": 0})
    res.setdefault("Access_Control-Allow-Origin", "*")
    return res
   # return JsonResponse({"msg":"资源名可以使用","status":True})







