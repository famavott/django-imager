"""Urls for imager_profile."""
from django.conf.urls import url

from imager_profile.views import profile_view, public_profile_view


urlpatterns = [
    url(r'^$', profile_view, name='profile'),
    url(r'^(?P<username>\w+)$', public_profile_view, name='user_profile')
]
