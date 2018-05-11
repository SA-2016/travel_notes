#coding=utf-8
from datetime import datetime

from django.db import models

from user.models import User
from article.models import Article

# Create your models here.


class Like(models.Model):
    userLike = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='点赞人')
    beLike = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='被赞文章')
    likeTime = models.DateTimeField(default=datetime.now, verbose_name='点赞时间')

    class Meta:
        verbose_name = '点赞动作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userLike


# class Attention(models.Model):
#     userAtten = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='关注人')
#     beAtten = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='被关注人')
#     attenTime = models.DateTimeField(default=datetime.now,verbose_name='关注时间')
#
#     class Meta:
#         verbose_name_plural='关注动作'
