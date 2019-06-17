from django.db import models


# Create your models here.
class FriendLink(models.Model):
    link_name = models.CharField(max_length=12)
    link_address = models.CharField(max_length=50)
    link_mark = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True, verbose_name="是否公开")

    def __str__(self):
        return '<FriendLink: %s>' % self.link_name

    class Meta:
        ordering = ['-add_time',]
        verbose_name_plural = '友情链接'
