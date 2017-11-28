"""Test file for imager_profile app."""
from django.test import Client, TestCase

import factory

from imager_profile.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """User factory class for use throughout tests."""

    class Meta:
        """Set model to User model."""

        model = User
    username = 'guy1'


class ProfileTests(TestCase):
    """Tests for ImagerProfile."""

    def setUp(self):
        """Setup for ProfileTests."""
        self.user = UserFactory.create()
        self.user.set_password('pass')
        self.user.save()

    def test_user_can_point_to_profile(self):
        """Test user can point to profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_user_has_camera_choice(self):
        """Test if user has correct default camera on profile."""
        one_user = User.objects.get(username='guy1')
        self.assertTrue(one_user.profile.camera_choices == 'CANON')

    def test_user_has_service_choice(self):
        """Test if user has correct default services on profile."""
        one_user = User.objects.first()
        self.assertTrue(one_user.profile.services_choices == 'PORTRAIT')

    def test_user_has_photo_styles_choice(self):
        """Test if user has correct default photos on profile."""
        one_user = User.objects.first()
        self.assertTrue(one_user.profile.photo_styles == 'BW')

    def test_user_bio_is_not_none(self):
        """Test if profile bio exists."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.bio)

    def test_user_phone_is_empty(self):
        """Test if profile phone is empty."""
        one_user = User.objects.first()
        self.assertFalse(one_user.profile.phone)

    def test_user_website_is_empty(self):
        """Test if profile website."""
        one_user = User.objects.first()
        self.assertFalse(one_user.profile.website)

    def test_user_is_active(self):
        """Test if profile is active for user."""
        one_user = User.objects.first()
        self.assertEqual(one_user.profile.is_active, True)


class Viewtests(TestCase):
    """Front-end tests using TestCase."""

    def test_home_route_200(self):
        """Test home route sends 200 response."""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route_has_home_link(self):
        """Test home route has home link in page."""
        c = Client()
        response = c.get('/')
        self.assertContains(response, '<a href="/">Home</a>')

    def test_login_route_200(self):
        """Test login route sends 200 response."""
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_returns_login_template(self):
        """Test login route returns login template."""
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.template_name, ['registration/login.html'])

    def test_logout_route_200(self):
        """Test logout route returns 200 response."""
        c = Client()
        response = c.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_logout_route_returns_logout_template(self):
        """Test logout route returns logout template."""
        c = Client()
        response = c.get('/logout/')
        self.assertEqual(response.template_name, ['registration/logged_out.html'])

    def test_register_route_200(self):
        """Test register route returns 200 response."""
        c = Client()
        response = c.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_route_returns_register_template(self):
        """Test register route returns register template."""
        c = Client()
        response = c.get('/accounts/register/')
        self.assertEqual(response.template_name, ['registration/registration_form.html'])
