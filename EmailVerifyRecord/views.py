from django.shortcuts import render
from django.core.mail import send_mail
from django.views import View
from django.http import HttpResponse

from .models import EmailVerifyRecord
from travel_notes.settings import EMAIL_FROM
from user.models import User
#from user.views import login_page

from random import Random
# Create your views here.


def random_str(random_length=8):

    # 生成随机字符串

    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,len(chars) - 1)]
    return str


def send_register_email(email, send_type=True):

    # 邮件生成发送

    email_record = EmailVerifyRecord()
    email_record.code = random_str(16)
    email_record.email = email
    email_record.type = send_type
    email_record.save()
    if send_type:
        email_title = '来自travel_notes的注册激活链接'
        email_body = "请点击下面的链接激活你的账号（若非本人操作请忽视）:" \
                     "http://127.0.0.1:8000/active/{0}".format(email_record.code)
        return send_mail(email_title,email_body,EMAIL_FROM,[email])
    else:
        return False


class ActiveUserView(View):

    # 用户激活认证

    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        context='服务异常，请联系管理员'
        if all_records:
            for record in all_records:
                email = record.email
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                context = '已激活，请前往网站登陆:http://127.0.0.1:8000/user/login_page/'
        else:
            context = '无效的激活邮件,前往网站:http://127.0.0.1:8000/'
        return HttpResponse(context)
