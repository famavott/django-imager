"""Urls for imager profile app."""
from django.conf.urls import include, url

from django.contrib import admin

from imagersite import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^$accounts/', include('registration.backends.hmac.urls')),
    # url(r'^login/$', placeholder, name='login'),
    # url(r'^logout/$', placeholder, name='logout')
]
