"""Urls for imager_profile."""
from django.conf.urls import url

from imager_profile.views import ProfileView, PublicProView


urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^(?P<username>\w+)$', PublicProView.as_view(), name='user_profile')
]
