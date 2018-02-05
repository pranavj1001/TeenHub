from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_news, name='show_news_page'),
    url(r'^save/news/list/all$', views.save_all_news_list, name='save_all_news_list'),
    url(r'^save/news/list/entertain$', views.save_entertain_news_list, name='save_entertain_news_list'),
    url(r'^save/news/list/tech$', views.save_tech_news_list, name='save_tech_news_list'),
]
