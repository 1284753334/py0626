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
from .forms import ResourceForm
from datetime import  datetime
from django.utils.http import urlquote
import re
from py1905.decorators import auth_sesson
from .templatetags import resource_extra


# Create your views here.
@auth_sesson
@transaction.atomic
def upload(request):
    """
    完成文件上传
    :param request:
    :return:
    """
    # 获取页面传过来的参数
    # data= request.POST
    # # print(data)
    # print(data.get("resource"))
    # with open(data.get("resource")) as f:
    #     f.read()
    #
    #
    #
    # # 2.创建一个模型对象,用来存储数据
    # res=Resource(
    #     resourceName= data.get("resourceName"),
    #     resourceType=data.get("resourceType"),
    #     resourceTime=datetime.now(),
    #     resourceSize=100,
    #     resource =data.get("resource"),
    #     Socre=data.get("Score"),
    #     keywords=data.get("keywords"),
    #     resourceDesc=data.get("resourceDesc"),
    # )
    # res.save()
    #
    # # 测试成功，页面跳转到首页

  # ModelForm 实现文件上传
    # 1.获取页面传过来的参数
    fm = ResourceForm(request.POST , request.FILES)
    file =request.FILES.get("resource")
    # print(file.name,file.size,file.content_type)

    #  2. 验证表单数据
    if fm.is_valid():
        # 3.验证通过将数据保存到数据库中

        # 设置上传文件的大小  获取上传文件的具体大小 赋值给数据库字段，用来保存到数据库
        fm.instance.resourceSize=fm.instance.resource.size

        # 设置上传时间
        fm.instance.resourceTime = datetime.now()

        # 设置user 设置一个存在的user
        userId= request.session.get("loginFlag").get("id")
        fm.instance.user = User.objects.get(id=userId)

        # 设置上传的类型

        fm.instance.content_type = request.FILES.get("resource").content_type


        fm.save()

        # fm.instance.save() instance 返回一个模型对象
        # 注册成功、页面跳转到首页
        return redirect(to="/")
    #否则 跳转到注册页面
    return render(request,"upload.html",{"msg":"上传失败"})

@auth_sesson
@transaction.atomic
def detail(request,id):
    # 根据资源id 查询资源
    res= Resource.objects.get(id=id)

    return render(request,"detail.html",{'res':res})

@auth_sesson
@transaction.atomic
def download(request,id):
    # 根据资源id 查询资源
    res= Resource.objects.get(id=id)

    # 获取资源路径
    with res.resource.open() as f:
        content = f.read()
        resp =HttpResponse(content)
        # 获取文件路径，并替换   /upload
        url = res.resource.name
        print(url)
        print(type(url))
        # re.sub(r'\s+', '-', text)
        #name = url.replace("/upload/", "")
        name = re.sub("/upload/", "",url)
        print(name)
        # name =res.resource.name.replace("/upload","")
        # print(type(name))
        # print(name)
        # 解决下载中文乱码问题
        resp["Content-Disposition"]="inline;filename=%s.format(urlquote(res.resourceName))"
        # 设置下载的头信息
        # 实现下载(attachment)
        # resp.setdefault("Content-Disposition","attachment;filename=name")

        # 在线预览
        resp["Content-Type"] = "application/octet-stream"
        resp["Content-Disposition"]= "attachment;filename="+urlquote(name)


        return resp



    return render(request,"download.html",{'res':res,"name":name})




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


def test(request):
    return HttpResponse(request,"test.html")


@transaction.atomic
@auth_sesson
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
        return JsonResponse({"msg": "资源名已存在", "status": False})
    return JsonResponse({"msg": "资源名可以使用", "status": True})

        # return HttpResponse(Callback + '{"msg":"资源名已存在","status":False}')
        # res= JsonResponse({"msg":"资源名已存在","status":0})
        # res.setdefault("Access_Control-Allow-Origin","*")
        # return res


    # return HttpResponse(Callback + '{"msg": "资源名可以使用", "status": True}')
    # res = JsonResponse({"msg": "资源名不存在", "status": 0})
    # res.setdefault("Access_Control-Allow-Origin", "*")
    # return res
   # return JsonResponse({"msg":"资源名可以使用","status":True})







