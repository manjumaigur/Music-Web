from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums' : albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    return render(request, 'music/detail.html', {'album' : album})

def favourite(request, album_id):
	album = get_object_or_404(Album, pk = album_id)
	try:
		selected_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', { 
			'album' : album , 
			'error_message' : 'Your Song Does Not Exist',
		})
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album' : album})
