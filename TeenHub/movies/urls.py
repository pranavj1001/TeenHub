from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^S$', views.show_movies, name='show_movies_page'),
]