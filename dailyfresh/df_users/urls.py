# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'login/$', views.login),
    url(r'register_submit/$', views.register_submit),
]