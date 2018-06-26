from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    profile_pic = models.FileField(default='')

    def __str__(self):
        return '{}\'s Profile'.format(self.user.username)