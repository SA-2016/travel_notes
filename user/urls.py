from django.contrib import admin
from django.urls import path,include,re_path
from user import views

app_name = 'user'
urlpatterns = [
    re_path(r'(?P<user_id>\d+)/$', views.user_info, name='user_info'),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('be_login/', views.login_page, name='login'),
    path('be_register/', views.register_page, name='register'),
    path('<str:user_email>/', views.personal_center, name='personal_center')

]
