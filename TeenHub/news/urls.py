from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_news, name='show_news_page'),
]