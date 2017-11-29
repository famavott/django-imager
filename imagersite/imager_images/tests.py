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
        for i in range(10):
            photo = PhotoFactory.build()
            photo.user = some_pro
            photo.save()
            album.photo.add(photo)
        self.album = album

    def test_if_album_exists(self):
        """Test if album created."""
        test_album = Album.objects.get()
        self.assertIsNotNone(test_album)

    def test_if_album_title_matches(self):
        """Test if album title is correct."""
        test_album = Album.objects.get()
        self.assertEqual(test_album.title, 'Some Title')

    def test_if_album_associated_with_user_has_profile_attrs(self):
        """Test if album associated with user that has attributes of image profile."""
        test_album = Album.objects.get()
        self.assertEqual(test_album.user.services_choices, 'PORTRAIT')

    def test_if_album_has_photos(self):
        """Test if album has photos."""
        test_album = Album.objects.get()
        self.assertTrue(test_album.photo.count() == 10)

    def test_if_album_associated_with_user_has_username(self):
        """Test if username associated with album is correct."""
        test_album = Album.objects.get()
        self.assertTrue(test_album.user.user.username, 'user1')
