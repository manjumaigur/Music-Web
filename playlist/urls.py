from django.conf.urls import url
from . import views

app_name = 'playlist'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<pk>\d+)/$', views.playlist_detail, name="detail"),
	url(r'^create/$', views.playlist_create, name="create"),
	url(r'^create-album/$', views.create_album, name="create_album"),
	url(r'^create-singer/$', views.create_singer, name="create_singer"),
	url(r'^create-artist/$', views.create_artist, name="create_artist"),
	url(r'^create-genre/$', views.create_genre, name="create_genre"),
	url(r'^create-favourite/$', views.create_favourite, name="create_favourite"),
	url(r'^create-random/$', views.create_random, name="create_random"),
]