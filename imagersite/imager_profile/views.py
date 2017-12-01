"""Views for imager_profile."""
from django.shortcuts import render


def profile_view(request, username=None):
    """View for the profile page."""
    return render(request, 'imager_profile/profile.html')
