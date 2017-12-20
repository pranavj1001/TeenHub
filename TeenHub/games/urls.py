from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games_home, name='show_games_page'),
]
