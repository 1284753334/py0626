from django.db import models
from datetime import datetime

# Create your models here.
'''
  
'''
class User(models.Model):
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    tel = models.CharField(max_length=11)
    Email= models.EmailField()
    sex_types = (
        ("1", "男"),
        ("2", "女")
    )


    sex =models.CharField(choices=sex_types,max_length=2)
    birth=models.DateField()

    # 为了看到效果
    def __str__(self):
        return  f"id,{self.id},username:{self.username},password:{self.password}"

    class Meta:
        db_table="t_user"

class Resource(models.Model):

    resourceName = models.CharField(max_length=32)
    types = [
        ("1","文本文件"),
        ("2","电子文件"),
        ("3","压缩文件"),
    ]


    resourceType = models.CharField(max_length=50,choices=types)

    keywords = models.CharField(max_length=100)

    Socre = models.IntegerField()

    resourceDesc = models.TextField(null=True)

    resourceTime = models.DateTimeField()

    resourceSize = models.IntegerField()

    # 资源，FileField对应的数据库字段也是一个字符串
    resource = models.FileField()


    # 上传者

    # 外键关联 表中维护一个字段。类中维护一个对象 默认和表中的id做关联，如果表中的主键做了改变，需要指定to_field
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"resourceName:{self.resourceName},resourceType:{self.resourceType}"

    class Meta:
        db_table = "t_resource"




class Sun(models.Model):
    name = models.CharField(max_length=4)

    class Meta:
        db_table="t_sun"

class Moon(models.Model):
    name= models.CharField(max_length=4)
    sun = models.OneToOneField(to= Sun,on_delete=models.CASCADE)
    class Meta:
        db_table="t_moon"

class Teacher (models.Model):
    t_name = models.CharField(max_length=21)
    class Meta:
        db_table="t_Teacher"

class Student (models.Model):
    s_name = models.CharField(max_length=21)
    sta = models.ManyToManyField(to=Teacher)
    class Meta:
        db_table="t_student"













