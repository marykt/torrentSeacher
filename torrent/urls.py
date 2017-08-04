from django.conf.urls import url
from django.contrib import admin
from torrent import views
from django.conf.urls import url, include
urlpatterns = [
    url(r'^search/', include('haystack.urls')),
    url(r'^$', views.index),
]
