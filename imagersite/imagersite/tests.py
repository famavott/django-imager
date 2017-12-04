"""Test module for imagersite front-end."""
from django.contrib.auth.models import User

from django.core import mail

from django.test import Client, TestCase

from django.urls import reverse_lazy

from imagersite.views import home_view


class Viewtests(TestCase):
    """Front-end tests using TestCase."""

    def setUp(self):
        """."""
        self.cleint = Client()

    def test_home_route_200(self):
        """Test home route sends 200 response."""
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_route_has_home_link(self):
        """Test home route has home link in page."""
        response = self.client.get(reverse_lazy('home'))
        self.assertContains(response, '<a href="/">Home</a>')

    def test_login_route_200(self):
        """Test login route sends 200 response."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_returns_login_template(self):
        """Test login route returns login template."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.template_name, ['registration/login.html'])

    def test_logout_route_200(self):
        """Test logout route returns 200 response."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 200)

    def test_logout_route_returns_logout_template(self):
        """Test logout route returns logout template."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.template_name, ['registration/logged_out.html'])

    def test_register_route_200(self):
        """Test register route returns 200 response."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_register_route_returns_register_template(self):
        """Test register route returns register template."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.template_name, ['registration/registration_form.html'])
