from django.contrib import admin

from .models import LikeRecord, LikeCount

# Register your models here.
@admin.register(LikeRecord)
class LikeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_id', 'content_type', 'content_object', 'user', 'like_date')


@admin.register(LikeCount)
class LikeCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_id', 'content_type', 'content_object', 'like_num')