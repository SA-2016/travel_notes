# import xadmin
from .models import Article


from django.contrib import admin
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','writer','location','art_pop','is_copyright']
    list_per_page = 15
    list_filter = ['title','writer','location','art_pop','is_copyright']
    search_fields = ['title','writer','location','art_pop','is_copyright']


admin.site.register(Article, ArticleAdmin)