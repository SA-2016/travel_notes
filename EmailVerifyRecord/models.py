from django.db import models

from datetime import datetime
# Create your models here.


class EmailVerifyRecord(models.Model):

    send_type = ((True,'注册验证'),(False,'找回验证'))

    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    type = models.BooleanField(choices=send_type, verbose_name='邮件类型')
    time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}:{1}'.format(self.email, self.code)