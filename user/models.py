#coding=utf-8
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Intuser(AbstractUser):
#     password = models.CharField(max_length=20,verbose_name='密码')
#     age = models.IntegerField(verbose_name='年龄')
#     email = models.EmailField(verbose_name='邮箱')
#     register = models.DateTimeField(default=datetime.now,verbose_name='注册时间')
#
#     def __str__(self):
#         return self.username


class User(models.Model):

    is_active_code = ((False, '未激活'),(True, '已激活'))

    name = models.CharField(max_length=50, default='Secret Superstar', verbose_name='名字')
    password = models.CharField(max_length=200, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')
    register = models.DateTimeField(default=datetime.now, verbose_name='注册时间')
    is_active = models.BooleanField(default=False, choices=is_active_code, verbose_name='是否激活')
    session = models.CharField(max_length=100, verbose_name='session', null=True, blank=True)
    session_time = models.IntegerField(verbose_name='session创建时间', null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class Producer(models.Model):
#     name=models.ForeignKey(User,on_delete=models.CASCADE)
#     nick_name = models.CharField(max_length=12,default='Secret Superstar',verbose_name='笔名')
#     pro_pop = models.PositiveIntegerField(verbose_name='受关注数',default=0)
#     art_num = models.PositiveIntegerField(verbose_name='作品数', default=0)
#
#     def pro_pop_incr(self):
#         self.pro_pop_incr += 1
#         self.save(update_fields=['pro_pop_incr'])
#
#     def art_num_incr(self):
#         self.art_num_incr += 1
#         self.save(update_fields=['art_num_incr'])
#
#     class Meta:
#         verbose_name = '创作者信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.nick_name



