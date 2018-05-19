from django.shortcuts import render,HttpResponse

from travel_notes.tasks import *
from operation.models import Like
from recommend.views import Reocmmends
from recommend.models import Recommend
# Create your views here.






@is_login
def content(request, email, id):
    art = Article.objects.get(id=id)
    temp = Reocmmends(id).recommend()
    if Recommend.objects.get(article_id=id) and len(temp) != 0:
        # temp1 = Reocmmends(id)
        # temp = temp1.recommend()
        or_like = []
        for i in temp:
            article = Article.objects.get(id=i)
            or_like.append(article)
    else:
        or_like = False
    context = {'art': art,
               'email': email,
               'or_like': or_like}
    context['like'] = True if Like.objects.get(userLike_id=User.objects.get(email=email).id, beLike_id=art.id) else False
    return render(request, 'content.html', context)


@is_login
def html_editor(request, email):
    context = {'email': email}
    return render(request,'start_create.html',context)


@is_login
def html_editor_handle(request, email):
    temp = Article()
    temp.writer_id = User.objects.get(email=email).id
    temp.title = request.POST['hname']
    temp.is_copyright_type = '1'
    body = request.POST['hcontent']
    temp.body = body
    temp.save()
    context = {'foo': temp,
               'email': email}
    return render(request, 'new_content.html', context)