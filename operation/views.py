from travel_notes.tasks import *
from .models import Like

from django.shortcuts import render
from django.http import JsonResponse


@is_login
def ajax_like(request, email):
    art_id = request.POST.get('art_id', '')
    art = Article.objects.get(id=art_id)
    user = User.objects.get(email=email)
    if art and user:
        temp = Like.objects.get(userLike_id=user.id, beLike_id=art_id)
        if temp:
            temp.delete()
            art.pop_decrease()
            key = '文章不错，点个赞吧！'
        else:
            like = Like()
            like.beLike_id = art.id
            like.userLike_id = user.id
            art.pop_increase()
            like.save()
            key = '已经赞过啦~,点击消赞'
    else:
        key = '非法操作'
    return JsonResponse({'back': key})


def index(request):
    temp = is_index_login(request)
    context = {'listPop': most_pop(10)}
    context['email'] = temp if temp else False
    return render(request, 'index.html', context)


def is_index_login(request):
    session = request.COOKIES.get('sessionid', '')
    user = User.objects.get(session=session) if session is not None else False
    return user.email if user and session_time_is_due(request, session) else False


@is_login
def exit(request, email):
    user = User.objects.get(email=email)
    user.session = None
    user.save()
    return index(request)