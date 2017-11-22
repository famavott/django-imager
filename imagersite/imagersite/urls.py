"""Urls for imager profile app."""
from django.conf.urls import url

from django.contrib import admin

from imagersite import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home')
]
