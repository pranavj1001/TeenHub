from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_dashboard, name='show_dashboard'),
    url(r'^view_full_news/$', views.show_dashboard_with_full_news, name='show_dashboard_with_full_news'),
    url(r'^movies/$', views.show_dashboard_movies, name='show_dashboard_movies'),
    url(r'^movies/(?P<year>\d+)/$', views.show_dashboard_movies_custom_year, name='show_dashboard_movies_custom_year'),
    url(r'^changePassword/$', views.show_dashboard_change_password, name='show_dashboard_change_password'),
    url(r'^passwordOperation/$', views.change_password, name='change_password'),
]