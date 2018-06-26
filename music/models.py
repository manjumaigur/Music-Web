from django.conf import settings
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False, null=True)
    artist = models.CharField(max_length=250,default='')
    album_logo = models.FileField(default='')
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk} )

    def __str__(self):
        return self.album_title

class Song(models.Model):
    song_title = models.CharField(max_length=500)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50,default='')
    singer = models.CharField(max_length=200,default='')
    audio_file = models.FileField(default='')
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk} )

    def __str__(self):
        return self.song_title
