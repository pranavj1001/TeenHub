from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.show_login, name='show_login'),
    url(r'^signup$', views.show_signup, name='show_signup'),
    url(r'^signupUser$', views.signup_user, name='signup_user'),
    url(r'^loginUser$', views.login_user, name='login_user'),
]