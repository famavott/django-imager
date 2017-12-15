"""Urls for imager_images app."""
from django.conf.urls import url

from django.contrib.auth.decorators import login_required

from imager_images.views import AlbumInfo, AlbumsView, CreateAlbum, CreatePhoto, LibraryView, PhotoInfo, PhotosView

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos/$', PhotosView.as_view(), name='photos'),
    url(r'^albums/$', AlbumsView.as_view(), name='albums'),
    url(r'^photos/(?P<pk>\d+)$', PhotoInfo.as_view(), name='photo_info'),
    url(r'^albums/(?P<pk>\d+)$', AlbumInfo.as_view(), name='album_info'),
    url(r'^photos/add/$', login_required(CreatePhoto.as_view()), name='create_photo'),
    url(r'^albums/add/$', login_required(CreateAlbum.as_view()), name='create_album')
]
