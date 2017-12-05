"""Views for imager_images."""
from django.shortcuts import render

from django.views.generic import ListView

from imager_images.models import Album, Photo


def library_view(request):
    """View for the library page."""
    user = request.user.profile
    photos = Photo.objects.filter(user=user)
    albums = Album.objects.filter(user=user)
    return render(request, 'imager_images/library.html',
                  context={'photos': photos,
                           'albums': albums})


# class LibraryView(ListView):
#   """."""

#   template_name = 'imager_images/library.html'


def album_view(request):
    """View for the user's albums."""
    user = request.user.profile
    albums = Album.objects.filter(user=user)
    return render(request, 'imager_images/albums.html',
                  context={'albums': albums})


def photos_view(request):
    """View for the user's photos."""
    user = request.user.profile
    photos = Photo.objects.filter(user=user)
    return render(request, 'imager_images/photos.html',
                  context={'photos': photos})


def album_info(request, id):
    """View for specific album info."""
    albums = Album.objects.get(id=id)
    photos = albums.photo.all()
    return render(request, 'imager_images/album_info.html',
                  context={'albums': albums,
                           'photos': photos})


def photo_info(request, id):
    """View for specific photo info."""
    photo = Photo.objects.get(id=id)
    return render(request, 'imager_images/photo_info.html',
                  context={'photo': photo})
