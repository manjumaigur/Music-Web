from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from .models import PlayList
from music.models import Song, Album
from .forms import  RandomSongsForm, AlbumMergeForm, SingerForm, FavouriteForm, GenreForm, ArtistForm

# Create your views here.

@login_required
def index(request):
	playlists = PlayList.objects.filter(user=request.user)
	query = request.GET.get("q")
	if query:
		songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
		if songs.count() == 0:
			messages.error(request, "No results found from your query. Please search different query")
		else:
			messages.success(request, "{} results found".format(songs.count()))
		return render(request,'music/all_songs.html',{'songs' : songs})
	return render(request, 'playlist/index.html', {'playlists':playlists})

@login_required
def playlist_detail(request,pk):
	playlist = get_object_or_404(PlayList, pk=pk)
	query = request.GET.get("q")
	if query:
		songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
		if songs.count() == 0:
			messages.error(request, "No results found from your query. Please search different query")
		else:
			messages.success(request, "{} results found".format(songs.count()))
		return render(request,'music/all_songs.html',{'songs' : songs})
	return render(request, 'playlist/playlist_detail.html', {'playlist':playlist})

@login_required
def playlist_create(request):
	messages.error(request, "Invalid access")
	return render(request, 'playlist/create.html',{})

@login_required
def create_album(request):
	if request.method == 'POST':
		form = AlbumMergeForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			albums = form.cleaned_data["albums"]
			new_playlist.save()
			for album in albums:
				for song in album.song_set.all():
					new_playlist.song.add(song)
					new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form = AlbumMergeForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})

@login_required
def create_singer(request):
	if request.method == 'POST':
		form = SingerForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			singer = form.cleaned_data["singer"]
			songs = Song.objects.filter(singer=singer)
			new_playlist.save()
			for song in songs:
				new_playlist.song.add(song)
				new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form = SingerForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})

@login_required
def create_artist(request):
	if request.method == 'POST':
		form = ArtistForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			artist = form.cleaned_data["artist"]
			albums = Album.objects.filter(artist=artist)
			new_playlist.save()
			for album in albums:
				for song in album.song_set.all():
					new_playlist.song.add(song)
					new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form = ArtistForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})

@login_required
def create_genre(request):
	if request.method == 'POST':
		form = GenreForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			genre = form.cleaned_data["genre"]
			genre = genre.capitalize()
			songs = Song.objects.filter(genre=genre)
			new_playlist.save()
			for song in songs:
				new_playlist.song.add(song)
				new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form = GenreForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})

@login_required
def create_favourite(request):
	if request.method == 'POST':
		form = FavouriteForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			songs = Song.objects.filter(is_favourite=True)
			new_playlist.save()
			for song in songs:
				new_playlist.song.add(song)
				new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form = FavouriteForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})

@login_required
def create_random(request):
	if request.method == 'POST':
		form =  RandomSongsForm(request.POST, request.FILES)
		if form.is_valid():
			new_playlist = form.save(commit=False)
			new_playlist.user = request.user
			songs = form.cleaned_data["songs"]
			new_playlist.save()
			for song in songs:
				new_playlist.song.add(song)
				new_playlist.save()
			new_playlist.save()
			return redirect('playlist:detail', pk=new_playlist.id)
	else:
		form =  RandomSongsForm()
	return render(request, 'playlist/playlist_form.html', {'form':form})