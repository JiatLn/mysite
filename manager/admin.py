from django.contrib import admin

from .models import FriendLink

# Register your models here.

@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_name', 'link_address', 'add_time', 'is_public')
    list_display_links = ('link_name', 'link_address')