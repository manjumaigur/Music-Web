from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['album_title','artist','album_logo',]

class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['song_title','audio_file','genre','singer',]
		