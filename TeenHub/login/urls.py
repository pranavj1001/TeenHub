from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.show_login, name='show_login'),
    url(r'^signup$', views.show_signup, name='show_signup'),
]