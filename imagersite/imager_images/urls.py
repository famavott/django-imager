"""Urls for imager_images app."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^library/$', views.library_view, name='library'),
    url(r'^photos/$', views.photos_view, name='photos'),
    url(r'^albums/$', views.album_view, name='albums'),
    url(r'^photos/(?P<id>\d+)$', views.photo_info, name='photo_info'),
    url(r'^albums/(?P<id>\d+)$', views.album_info, name='album_info')
]
