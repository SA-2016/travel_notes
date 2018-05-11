from django.db import models

from datetime import datetime

from user.models import User
from tinymce.models import HTMLField
# Create your models here.


class Article(models.Model):
    is_copyright_type = ((True, '是'),(False, '否'))

    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=10, verbose_name='标题')
    body = models.CharField(max_length=5000, verbose_name='正文')
    art_pop = models.PositiveIntegerField(verbose_name='点赞数', default=0)
    publishTime = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    location = models.CharField(max_length=20, null=True, blank=True, verbose_name='地点')
    is_copyright = models.BooleanField(choices=is_copyright_type, verbose_name='版权限制', default=False)

    def pop_increase(self):
        self.art_pop += 1
        self.save(update_fields=['art_pop'])

    def pop_decrease(self):
        self.art_pop -= 1
        self.save(update_fields=['art_pop'])

    class Meta:
        verbose_name='游记信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title


