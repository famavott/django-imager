"""Model for imager_profile app."""
from django.contrib.auth.models import User

from django.db import models


class ImageActiveProfile(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        super(ImageActiveProfile, self).get_queryset().filter(is_active=True)


class ImagerProfile(models.Model):
    """Create user model for imager profile."""

    website = models.URLField()
    location = models.CharField(max_length=100)
    fee = models.FloatField()
    CAMERA_CHOICES = (
        ('CANON', 'Canon'),
        ('NIKON', 'Nikon'),
        ('OLYMPUS', 'Olyumpus')
    )
    camera_choices = models.CharField(
        max_length=2,
        choices=CAMERA_CHOICES,
        default='CANON')
    SERVICES_CHOICES = (
        ('PORTRAIT', 'Portrait'),
        ('WEDDING', 'Wedding'),
        ('AWKWARD', 'Awkward')
    )
    services_choices = models.CharField(
        max_length=2,
        choices=SERVICES_CHOICES,
        default='PORTRAIT')
    bio = models.TextField()
    phone = models.CharField(max_length=100)
    PHOTO_STYLES = (
        ('BW', 'Black and White'),
        ('Color', 'Color')
    )
    photo_styles = models.CharField(
        max_length=2,
        choices=PHOTO_STYLES,
        default='BW')
    user = models.OneToOneField(User)
    active = ImageActiveProfile()

    @property
    def is_active(self):
        """."""
        return self.user.is_active
