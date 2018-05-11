from django.contrib import admin
from django.urls import path,include,re_path
from article import views


app_name = 'article'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #re_path('(?P<username>.*)/',views.gets)
    #re_path('^$',),
    # path('login_page/',views.login_page,name='login_page'),
    # path('register_page/',views.register_page,name='register_page'),
    # path('be_writer/',views.be_writer,name='be_writer'),
    re_path(r'^(?P<id>\d+)/$', views.content, name='id'),
    path('htmlEditor/', views.html_editor, name='writing'),
    path('htmlEditorHandle/', views.html_editor_handle, name='publish'),
]
