"""Test file for imager_images app."""
from django.test import TestCase

import factory

from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile, User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Photo factory class for use throughout tests."""

    class Meta:
        """Set model to Photo model."""

        model = Photo


class PhotoTests(TestCase):
    """Tests for Photo model."""

    # @classmethod 1024

    # def setUp(self):
    #     """Setup for PhotoTests."""
    #     someuser = User(username='user1', password='somepassword')
    #     someuser.save()
    #     some_pro = someuser.profile
    #     some_pro.save()
    #     album = Album(user=some_pro, title='Some Title')
    #     album.save()
    #     for i in range(10):
    #         photo = PhotoFactory.build()
    #         photo.user = some_pro
    #         photo.save()
    #         album.photos.add(photo)
    #     self.album = album

    # def test_user_points_to_profile(self):
    #     """Test if user points to a profile."""
    #     test_user = User.objects.first()
    #     self.assertIsNotNone(test_user.profile)
