from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_dashboard, name='show_dashboard'),
]