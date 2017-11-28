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

    def setUp(self):
        """Setup for PhotoTests."""
        someuser = User(username='user1', password='somepassword')
        someuser.save()
        some_pro = someuser.profile
        some_pro.save()
        album = Album(user=some_pro, title='Some Title')
        album.save()
        photo = Photo(user=some_pro, title='Ugly Pics')
        photo.save()

    def test_user_points_to_profile(self):
        """Test if user points to a profile."""
        test_user = User.objects.first()
        self.assertIsNotNone(test_user.profile)

    # def test_user_has_photo_with_title(self):
    #     """Test if user has photo attrs."""
    #     test_user = User.objects.first()
    #     test_picture = test_user.profile.photo
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(test_picture.title, 'Some Title')
