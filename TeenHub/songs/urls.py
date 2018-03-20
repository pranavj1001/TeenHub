from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_songs, name='show_songs_page'),
    url(r'^infoSongs/(?P<songsinfo>.+)/(?P<name>.+)/(?P<type>.+)/$', views.show_song_info, name='show_song_info'),
]
