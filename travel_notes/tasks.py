from article.models import Article
from user.models import User
from celery import shared_task
from django.conf import settings
from operation.models import Like

from django.http import HttpResponse

import time
#__________________________________________________________________________________


def most_pop(num):
    return Article.objects.order_by('-art_pop','publishTime')[:num]


@shared_task
def session_time_is_due(request,session):
    now_time = int(time.time())
    user = User.objects.get(session=session)
    return False if now_time > user.session_time else True


@shared_task
def is_login(function_name):
    def func_in(request, *args, **kwargs):
        session = request.COOKIES.get('sessionid', '')
        user = User.objects.get(session=session)
        if user and session_time_is_due(request, session):
            return function_name(request, user.email, *args, **kwargs)
        return HttpResponse('请先登陆')
    return func_in


@shared_task
def create_session_time(request,email):
    session_time = int(time.time())
    user = User.objects.get(email=email)
    user.session_time = session_time + 3600
    user.session = request.COOKIES.get('sessionid', '')
    user.save()


@shared_task
def recommend(request):
    pass


@shared_task
def statistics(request,email):
    user = User.objects.get(email=email).id
    like = Like.objects.filter(userLike_id=user).latest('id')



