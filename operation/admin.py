# import xadmin
from .models import Like


from django.contrib import admin
# Register your models here.


class LikeAdmin(admin.ModelAdmin):
    list_display = ['userLike', 'beLike', 'likeTime']
    list_per_page = 15
    search_fields = ['userLike', 'beLike', 'likeTime']
    list_filter = ['userLike', 'beLike', 'likeTime']


admin.site.register(Like, LikeAdmin)


# class AttenAdmin(admin.ModelAdmin):
#     list_display = ['userAtten', 'beAtten', 'attenTime']
#     list_per_page = 15
#     search_fields = ['userAtten', 'beAtten', 'attenTime']
#     list_filter = ['userAtten', 'beAtten', 'attenTime']
#
#
# admin.site.register(Attention,AttenAdmin)