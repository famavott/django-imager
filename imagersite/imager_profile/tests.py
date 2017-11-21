"""Test file for imager_profile app."""
from django.test import TestCase

import factory

from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User
    username = factory.Sequence(lambda num: 'user{0}'.format(num))


class ProfileTests(TestCase):
    """."""

    def setUp(self):
        """."""
        profile = ImagerProfile()
        for num in range(20):
            user = UserFactory.create()
            user.set_password('pass')
            user.save()
        profile.user = user
        profile.save()

    def test_user_can_point_to_profile(self):
        """."""
        one_user = User.objects.get(id=20)
        self.assertIsNotNone(one_user.profile)
