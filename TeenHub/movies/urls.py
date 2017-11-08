from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.show_movies, name='show_movies_page'),
]