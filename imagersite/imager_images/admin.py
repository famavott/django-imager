"""Expose Photo and Album to admin screen."""
from django.contrib import admin

from .models import Album, Photo

admin.site.register(Album)
admin.site.register(Photo)
