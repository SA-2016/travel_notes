from django.shortcuts import render,HttpResponse


from travel_notes.function import *
from operation.models import Like

# Create your views here.






@is_login
def content(request, email, id):
    art = Article.objects.get(id=id)
    context = {'art': art,
               'email': email}
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