"""Models for imager_images app."""
from django.db import models

from imager_profile.models import ImagerProfile


class Photo(models.Model):
    """Create a photo model."""

    user = models.ForeignKey(ImagerProfile, related_name='photo')
    imgfile = models.ImageField(upload_to='images')
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True,
        default='PUBLIC'
    )

    def __str__(self):
        """Return name for object."""
        return self.title


class Album(models.Model):
    """Create an album model."""

    user = models.ForeignKey(ImagerProfile, related_name='album', on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo, related_name='album')
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True,
        default='PUBLIC'
    )

    def __str__(self):
        """Return name for object."""
        return self.title
