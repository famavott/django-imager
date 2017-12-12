""""Custom storage for S3."""
from django.conf import settings

from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    """Class for static storage."""

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    """Class for media storage."""

    location = settings.MEDIAFILES_LOCATION
