from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name='昵称', default='')

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)
