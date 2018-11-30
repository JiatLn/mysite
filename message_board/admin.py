from django.contrib import admin

from .models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'email', 'created_time', 'get_content', 'is_public')
    list_filter = ('created_time',)
    list_display_links = ('get_content',)