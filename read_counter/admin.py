from django.contrib import admin

from .models import ReadNum, ReadDetail

# Register your models here.
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_id', 'content_type', 'content_object', 'read_num')



@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'username', 'date')