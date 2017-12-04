"""Test file for imager_profile app."""
from django.test import TestCase

import factory

from imager_profile.models import ImagerProfile, User


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

    def test_active_manager(self):
        """Test if active manager has an active user."""
        self.assertTrue(ImagerProfile.active.count() == 1)
