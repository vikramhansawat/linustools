from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from linusauth.forms import LoginForm

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'linusauth/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/', auth_views.logout, {'next_page': '/login'}, name="logout"),
	]