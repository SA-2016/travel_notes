from django.contrib import admin
from django.urls import path,include,re_path

from operation import views

app_name = 'operation'
urlpatterns = [
    re_path('like/', views.ajax_like, name='like'),
    path('exit/', views.exit, name='exit')
]
