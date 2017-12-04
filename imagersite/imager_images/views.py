"""Views for imager_images."""
from django.shortcuts import render

from imager_images.models import Album, Photo


def library_view(request):
    """View for the library page."""
    user = request.user.profile
    photos = Photo.objects.filter(user=user)
    albums = Album.objects.filter(user=user)
    return render(request, 'imager_images/library.html',
                  context={'photos': photos,
                           'albums': albums})


def album_view(request):
    """View for the user's albums."""
    user = request.user.profile
    albums = Album.objects.filter(user=user)
    return render(request, 'imager_images/library.html',
                  context={'albums': albums})


def photos_view(request):
    """View for the user's photos."""
    user = request.user.profile
    photos = Album.objects.filter(user=user)
    return render(request, 'imager_images/photos.html',
                  context={'photos': photos})
