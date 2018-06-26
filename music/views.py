from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from .models import Album, Song
from .forms import AlbumForm, SongForm
# Create your views here.


#@method_decorator(login_required, name='dispatch')
#class AlbumIndex(generic.ListView):
 #default context_object_name='object_list'
 #    context_object_name = 'albums'	

 #   def get_queryset(self):
 #       qs=Album.objects.all()
 #       return qs.filter(user=self.request.user)

@login_required
def index(request):
    albums = Album.objects.filter(user=request.user)
    query = request.GET.get("q")
    if query:
        songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
        if songs.count() == 0:
            messages.error(request, "No results found from your query. Please search different query")
        else:
            messages.success(request, "{} results found".format(songs.count()))
        return render(request,'music/all_songs.html',{'songs' : songs})
    else:
        return render(request,'music/index.html', {'albums':albums})

@login_required
def album_detail(request,pk):
    album = get_object_or_404(Album, pk=pk)
    query = request.GET.get("q")
    if query:
        songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
        if songs.count() == 0:
            messages.error(request, "No results found from your query. Please search different query")
        else:
            messages.success(request, "{} results found".format(songs.count()))
        return render(request,'music/all_songs.html',{'songs' : songs})
    else:
        return render(request, 'music/detail.html',{'album':album})
    


@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.user = request.user
            new_album.save()
            return redirect('music:detail', pk=new_album.id)
    else:
        form = AlbumForm()
    return render(request, 'music/album_form.html', {'form' : form})

@login_required
def update_album(request,pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.save()
            return redirect('music:detail', pk=new_album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_form.html', {'form' : form})

@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

@login_required
def all_songs(request):
    user = request.user
    query = request.GET.get("q")
    if query:
        songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
        if songs.count() == 0:
            messages.error(request, "No results found from your query. Please search different query")
        else:
            messages.success(request, "{} results found".format(songs.count()))
        return render(request,'music/all_songs.html',{'songs' : songs})
    else:
        songs = Song.objects.filter(album__user=request.user)

        return render(request,'music/all_songs.html', {'songs':songs});

@login_required
def create_song(request,pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.album = album
            new_song.save()
            return redirect('music:detail', pk=album.id)
    else:
        form = SongForm()
    return render(request, 'music/song_form.html', {'form' : form})

@login_required
def update_song(request,pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.save()
            return redirect('music:detail', pk=song.album.id)
    else:
        form = SongForm(instance=song)
    return render(request, 'music/song_form.html', {'form' : form})

@method_decorator(login_required, name='dispatch')
class DeleteSong(DeleteView):
    model = Song

    def get_success_url(self):
        return reverse_lazy('music:detail',kwargs={'pk':self.get_object().album.id})

@login_required
def favourite(request, pk):
    song = get_object_or_404(Song, pk=pk)
    album = song.album
    song.is_favourite = not song.is_favourite
    song.save()
    return render(request,'music/detail.html', {'album': album})
