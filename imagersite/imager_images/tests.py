"""Test file for imager_images app."""
import tempfile

from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile as Sup

from django.test import Client, TestCase

from django.urls import reverse_lazy

import factory

from imager_images.models import Album, Photo

from imager_profile.models import User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Photo factory class for use throughout tests."""

    class Meta:
        """Set model to Photo model."""

        model = Photo


class PhotoTests(TestCase):
    """Tests for Photo, album, and related front-end pieces."""

    def setUp(self):
        """Setup for PhotoTests."""
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        self.client = Client()
        someuser = User(username='user1', password='somepassword')
        self.someuser = someuser
        someuser.save()
        some_pro = someuser.profile
        self.some_pro = some_pro
        some_pro.save()
        album = Album(user=some_pro, title='Some Title')
        album.cover = Sup(name='bad_photo.jpg',
                          content=open('media/images/louie.png',
                                       'rb').read(),
                          content_type='image/png')
        album.save()
        for i in range(10):
            photo = PhotoFactory.build()
            photo.user = some_pro
            photo.imgfile = Sup(name='bad_photo.jpg',
                                content=open('media/images/louie.png',
                                             'rb').read(),
                                content_type='image/png')
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

    def test_library_route_returns_template(self):
        """Test library route returns correct template."""
        self.client.force_login(self.someuser)
        response = self.client.get(reverse_lazy('library'))
        self.assertEqual(response.templates[0].name, 'imager_images/library.html')

    def test_album_route_returns_template(self):
        """Test album route returns template."""
        self.client.force_login(self.someuser)
        response = self.client.get(reverse_lazy('albums'))
        self.assertEqual(response.templates[0].name, 'imager_images/albums.html')

    def test_photos_route_returns_template(self):
        """Test album route returns template."""
        self.client.force_login(self.someuser)
        response = self.client.get(reverse_lazy('photos'))
        self.assertEqual(response.templates[0].name, 'imager_images/photos.html')

    def test_photo_info_route_returns_template(self):
        """Test album route returns template."""
        self.client.force_login(self.someuser)
        pid = Photo.objects.first().id
        response = self.client.get(reverse_lazy('photo_info',
                                                kwargs={'pk': pid}))
        self.assertTemplateUsed(response, 'imager_images/photo_info.html')

    def test_album_info_route_returns_template(self):
        """Test album route returns template."""
        self.client.force_login(self.someuser)
        pid = Album.objects.first().id
        response = self.client.get(reverse_lazy('album_info',
                                                kwargs={'pk': pid}))
        self.assertEqual(response.templates[0].name, 'imager_images/album_info.html')

    def test_add_photo_route_returns_200_if_logged_in(self):
        """Test add photo route returns 200 if user is logged in."""
        self.client.force_login(self.someuser)
        response = self.client.get(reverse_lazy('create_photo'))
        self.assertEqual(response.status_code, 200)

    def test_add_album_route_returns_200_if_logged_in(self):
        """Test add album route returns 200 if user is logged in."""
        self.client.force_login(self.someuser)
        response = self.client.get(reverse_lazy('create_album'))
        self.assertEqual(response.status_code, 200)

    def test_add_photo_route_returns_302_not_logged_in(self):
        """Test add photo route redirects to login."""
        response = self.client.get(reverse_lazy('create_photo'))
        self.assertEqual(response.status_code, 302)

    def test_add_album_route_returns_302_not_logged_in(self):
        """Test add album route redirects to login."""
        response = self.client.get(reverse_lazy('create_album'))
        self.assertEqual(response.status_code, 302)

    def test_successful_add_photo_redirects_to_lib(self):
        """Test user redirected to library after adding photo."""
        self.client.force_login(self.someuser)
        test_img = Sup(name='some_photo.jpg',
                       content=open('media/images/louie.png',
                                    'rb').read(),
                       content_type='image/png')
        passed_data = {
            'imgfile': test_img,
            'description': 'A photo',
            'title': 'Ugly people',
            'published': 'PRIVATE'
        }
        response = self.client.post(reverse_lazy('create_photo'), passed_data)
        self.assertEqual(response.status_code, 302)

    def test_successful_add_album_redirects_to_lib(self):
        """Test user redirected to library after adding album."""
        self.client.force_login(self.someuser)
        test_img = Sup(name='some_photo.jpg',
                       content=open('media/images/louie.png',
                                    'rb').read(),
                       content_type='image/png')
        passed_data = {
            'cover': test_img,
            'description': 'Album 5',
            'photo': 143,
            'title': 'Selfies',
            'published': 'PUBLIC'
        }
        response = self.client.post(reverse_lazy('create_album'), passed_data)
        self.assertEqual(response.status_code, 302)
