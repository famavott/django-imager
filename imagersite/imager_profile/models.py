"""Model for imager_profile app."""
from django.contrib.auth.models import User

from django.db import models


class ProfileManager(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Create user model for imager profile."""

    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    CAMERA_CHOICES = (
        ('CANON', 'Canon'),
        ('NIKON', 'Nikon'),
        ('OLYMPUS', 'Olyumpus'),
        ('FUJI', 'Fuji')
    )
    camera_choices = models.CharField(
        max_length=50,
        choices=CAMERA_CHOICES,
        default='CANON')
    SERVICES_CHOICES = (
        ('PORTRAIT', 'Portrait'),
        ('WEDDING', 'Wedding'),
        ('AWKWARD', 'Awkward')
    )
    services_choices = models.CharField(
        max_length=50,
        choices=SERVICES_CHOICES,
        default='PORTRAIT')
    bio = models.TextField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    PHOTO_STYLES = (
        ('BW', 'Black and White'),
        ('Color', 'Color')
    )
    photo_styles = models.CharField(
        max_length=50,
        choices=PHOTO_STYLES,
        default='BW')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    active = ProfileManager()

    @property
    def is_active(self):
        """Active method for ImagerProfile."""
        return self.user.is_active
