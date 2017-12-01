"""Views for imager_profile."""
from django.contrib.auth.models import User

from django.shortcuts import render

from imager_images import Album, Photo


def profile_view(request):
    """View for the profile page."""
    return render(request, 'imager_profile/profile.html')


def public_profile_view(request, username=None):
    """View for the user profile page(public)."""
    user = User.objects.get(username=username)
    photo = Photo.objects.get.filter(published='PUBLIC')
    album = Album.objects.get.filter(published='PUBLIC')
    return render(request, 'imager_profile/public_profile.html',
                  context={'user': user,
                           'photo': photo,
                           'album': album})
