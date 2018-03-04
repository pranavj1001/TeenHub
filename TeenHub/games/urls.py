from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games_home, name='show_games_page'),
    url(r'^infoGames/(?P<gameid>\d+)/$', views.show_game_info, name='show_game_info'),
]
