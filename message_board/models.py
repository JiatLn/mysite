from django.db import models

# Create your models here.

class Message(models.Model):
    nickname = models.CharField(max_length=20, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱", editable=True)
    content = models.TextField(verbose_name="留言")
    created_time = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True, verbose_name="是否公开")


    def __str__(self):
        return '<Message: %s>' % self.content

    def get_content(self):
        if len(self.content) > 30:
            return self.content[:30] + '...'
        else:
            return self.content

    class Meta:
        ordering = ['-created_time',]
        verbose_name_plural = '留言'