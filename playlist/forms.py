from django import forms
from music.models import Song, Album
from .models import PlayList

class AlbumMergeForm(forms.ModelForm):
	albums = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Album.objects.all())
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo', 'albums']

class SingerForm(forms.ModelForm):
	singer = forms.CharField(max_length=200)
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo', 'singer']

class ArtistForm(forms.ModelForm):
	artist = forms.CharField(max_length=200)
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo', 'artist']

class FavouriteForm(forms.ModelForm):
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo']

class GenreForm(forms.ModelForm):
	genre = forms.CharField(max_length=200)
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo', 'genre']

class RandomSongsForm(forms.ModelForm):
	songs = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Song.objects.all())
	class Meta:
		model = PlayList
		fields = ['playlist_name', 'playlist_logo', 'songs']