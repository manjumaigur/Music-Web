from django.conf.urls import url
from . import views
from accounts.views import login_view

app_name = 'music'

urlpatterns = [
    url(r'^accounts/login/$',login_view, name='login'),
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/songs/
    url(r'^songs/$', views.all_songs, name='songs'),
    # /music/album_id/
    url(r'^(?P<pk>\d+)/$', views.album_detail, name='detail'),
    # /music/add-album/
    url(r'^add-album/$', views.create_album, name='add-album'),
    # /music/6/edit-album
    url(r'^(?P<pk>\d+)/edit-album/$', views.update_album, name='edit-album'),
    # /music/album/6/delete-album/
    url(r'^album/(?P<pk>\d+)/delete-album/$', views.DeleteAlbum.as_view(), name='delete-album'),
    # /music/6/add-song/
    url(r'^(?P<pk>\d+)/add-song/$', views.create_song, name='add-song'),
    # /music/6/edit-song
    url(r'^(?P<pk>\d+)/edit-song/$', views.update_song, name='edit-song'),
    # /music/6/delete-song
    url(r'^(?P<pk>\d+)/delete-song/$', views.DeleteSong.as_view(), name='delete-song'),
    # /music/song_id/favourite
    url(r'^(?P<pk>\d+)/favourite/$', views.favourite, name='favourite'),

 ]