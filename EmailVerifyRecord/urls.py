from django.contrib import admin
from django.urls import path,include,re_path

from .views import ActiveUserView

app_name = 'active'
urlpatterns = [
    re_path(r'(?P<active_code>\w+)/',ActiveUserView.as_view(),name='ActiveUser'),
]
