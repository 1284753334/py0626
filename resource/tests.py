from django.test import TestCase
from .models import User

# 是django 自带的测试模块

"""
在企业中，做web开发，至少会有2套完全相同的数据库
"""

# Create your tests here.
#  方法一  保存数据
# class Test(TestCase):
    #  不定义方法 不会自动销毁数据
#   def test(self):
#     user = User(username="zhangsan",password="lisi")
#     user.save()
#     # 获取保存后、数据库的主键
#     print('first:',user,user.id)
#
#     # 修改password 的密码为123456
#     user=User(id =1,password="lisi")
#
#     user.password="123456"
#     # 更新后执行保存操作
#     user.save()
#
#     print("sec:",user,user.id)
#
#     print(User.objects.all())

# 方法二 插入数据库

# 模型.object.create()来插入  会自动保存

class Test(TestCase):
    def test(self):
        # # // 保存数据库，不调用save 方法
        # user= User.objects.create(username="zhangsan",password="lisi")
        # # 查询数据
        # print(User.objects.all(),user.id)
        # user2 = User.objects.create(id=1,username="zhangsan", password="123456")
        #
        # print(User.objects.all(),user2.id)

        user = User.objects.create(username="zhangsan", password="lisi")
        user.delete()


        # User.objects.create(username="zhangsan",password="lisi")

        # u=User.objects.update(username="王五",id=2)

        print(User.objects.all())