from django.db import models
from django.conf import settings
from django.urls import reverse
from music.models import Song

# Create your models here.

class PlayList(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False, null=True)
	playlist_name = models.CharField(max_length = 200)
	playlist_logo = models.FileField(default='')
	song = models.ManyToManyField(Song)
	is_favourite = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('playlist:detail', kwargs={'pk':self.id})

	def __str__(self):
		return self.playlist_name
