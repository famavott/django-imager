"""Views for imager_profile."""
from django.contrib.auth.models import User

from django.shortcuts import render

from imager_images.models import Album, Photo


def profile_view(request):
    """View for the personal profile page."""
    user = request.user.profile
    pub_photo = (Photo.objects
                 .filter(published='PUBLIC')
                 .filter(user=user)).count()
    pub_album = (Photo.objects
                 .filter(published='PUBLIC')
                 .filter(user=user)).count()
    priv_photo = (Photo.objects
                  .filter(published='PRIVATE')
                  .filter(user=user)).count()
    pub_photo = (Photo.objects
                 .filter(published='PUBLIC')
                 .filter(user=user)).count()
    return render(request, 'imager_profile/profile.html',
                  context={'pub_photo': pub_photo,
                           'pub_album': pub_album,
                           'priv_photo': priv_photo,
                           'pub_photo': pub_photo})


def public_profile_view(request, username=None):
    """View for the user profile page(public)."""
    user = User.objects.get(username=username)
    photo = (Photo.objects
             .filter(published='PUBLIC')
             .filter(user=user.profile)).count()
    album = (Album.objects
             .filter(published='PUBLIC')
             .filter(user=user.profile)).count()
    return render(request, 'imager_profile/public_profile.html',
                  context={'user': user,
                           'photo': photo,
                           'album': album})
