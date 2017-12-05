"""Urls for imager_images app."""
from django.conf.urls import url

from imager_images.views import AlbumInfo, LibraryView, PhotoInfo, PhotosView

from . import views

# from imager_images.views import AlbumInfo, AlbumView, LibraryView, PhotoInfo, PhotosView

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos/$', PhotosView.as_view(), name='photos'),
    url(r'^albums/$', views.album_view, name='albums'),
    url(r'^photos/(?P<pk>\d+)$', PhotoInfo.as_view(), name='photo_info'),
    url(r'^albums/(?P<pk>\d+)$', AlbumInfo.as_view(), name='album_info')
]
