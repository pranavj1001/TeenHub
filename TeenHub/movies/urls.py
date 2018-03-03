from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout$', views.logout, name='logout'),
    url(r'^infoMovies/(?P<movieid>\d+)/$', views.show_movie_info, name='show_movie_info'),
    url(r'^save/movie/rating/(?P<movie_rating>\d+)/$', views.save_movie_rating, name='save_movie_rating'),
    url(r'^$', views.show_movies, name='show_movies_page'),
    url(r'^genres/(?P<genre_id>\d+)/$', views.show_genre_list, name='show_genre_list')
]