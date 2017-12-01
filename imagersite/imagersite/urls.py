"""Urls for imager site."""
from django.conf.urls import include, url

from django.contrib import admin

from django.contrib.auth import views as log_views

from imagersite import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^login/', log_views.login, name='login'),
    url(r'^logout/', log_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/', include('imager_profile.urls')),
    # url(r'^images/', include)
]
