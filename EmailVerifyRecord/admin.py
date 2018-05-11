# import xadmin
from .models import EmailVerifyRecord


from django.contrib import admin
# Register your models here.


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['email', 'type']
    list_per_page = 15
    list_filter = ['email', 'type']
    search_fields = ['email', 'type']


admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)