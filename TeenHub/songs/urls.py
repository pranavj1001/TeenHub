from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_songs, name='show_songs_page'),
]
