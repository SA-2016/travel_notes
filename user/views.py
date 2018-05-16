# -*-coding:utf-8 -*-

from django.shortcuts import render,HttpResponse
from  django.contrib.auth.hashers import make_password,check_password

from datetime import datetime


from travel_notes.tasks import *
from .models import User
from . import form
from EmailVerifyRecord.views import send_register_email
from operation.models import Like

# Create your views here.

# def login_page(request):
#     if request.method == 'GET':
#         obj = form.LoginForm()
#         return render(request, 'login_page.html', {'obj': obj})
#     elif request.method == 'POST':
#         email = request.POST.get('email', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username=email, password=password)
#         if user is not None:
#             login(request,user)
#             listPop = most_pop(10)
#             context = {'listPop': listPop }
#             return render(request, 'index.html', context)
#         return index(request)


# def test_login(request):
#     pass


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        temp = User.objects.get(email=email)
        if temp:
            if check_password(password,temp.password):
                if temp.is_active:
                    create_session_time(request,email)
                    context = {'listPop': most_pop(10), 'email':email}
                    return render(request, 'index.html', context)
                else:
                    return HttpResponse('用户未激活')
            else:
                request.method = 'GET'
                return login_page(request)
        else:
            request.method = 'GET'
            return register_page(request)
    else:
        return render(request, 'login_page.html', {'obj': form.LoginForm() })


def register_page(request):
    if request.method == 'POST':
        temp = User()
        temp.name = request.POST.get('name','')
        temp.password = make_password(request.POST.get('password', ''))
        temp.age = request.POST.get('age','')
        temp.email = request.POST.get('email','')
        temp.register = datetime.strptime(request.POST.get('register',''), '%Y/%m/%d %H:%M')
        if send_register_email(temp.email):
            temp.save()
            return HttpResponse('请前往邮箱激活')
        else:
            return HttpResponse('服务不可用')
    else:
        return render(request, 'register_page.html', {'obja': form.RegisterForm()})


@is_login
def user_info(request, email, user_id):
    art = Article.objects.filter(writer_id=user_id)
    context = {'writer_info': User.objects.get(id=user_id),
               'art_list': art,
               'email': email,
               'art_num':art.count()}
    return render(request, 'user_info.html', context )


@is_login
def personal_center(request, email, user_email):
    if email == user_email:
        user = User.objects.get(email=email)
        last_login_time =time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(user.session_time))
        art = Article.objects.filter(writer_id=user.id)
        like = Like.objects.filter(userLike=user.id)
        like_art = []
        for i in like:
            be_like = Article.objects.get(id=i.beLike_id)
            be_like.like_time = i.likeTime
            like_art.append(be_like)
        context = {
            'user_name': user.name,
            'user_age': user.age,
            'email': user.email,
            'register_time': user.register,
            'last_login_time': last_login_time,
            'art': art,
            'art_num': art.count(),
            'like_art': like_art,
            'like_num': like.count(),
        }
        return render(request, 'personal_center.html', context)
    return HttpResponse('非法查询')



