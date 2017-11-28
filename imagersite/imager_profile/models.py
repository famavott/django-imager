"""Model for imager_profile app."""
from django.contrib.auth.models import User

from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver


class ProfileManager(models.Manager):
    """Active user profile manager."""

    def get_queryset(self):
        """Get active users."""
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Create user model for imager profile."""

    objects = models.Manager()
    active = ProfileManager()
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    bio = models.TextField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
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
    PHOTO_STYLES = (
        ('BW', 'Black and White'),
        ('Color', 'Color')
    )
    photo_styles = models.CharField(
        max_length=50,
        choices=PHOTO_STYLES,
        default='BW')

    @property
    def is_active(self):
        """Active method for ImagerProfile."""
        return self.user.is_active


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Create profile whenever new user created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
