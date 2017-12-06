"""Views for imager_profile."""
from django.contrib.auth.models import User

from django.views.generic import TemplateView

from imager_profile.models import ImagerProfile


class ProfileView(TemplateView):
    """View for the personal profile page."""

    template_name = 'imager_profile/profile.html'


class PublicProView(TemplateView):
    """View for the public profile page."""

    template_name = 'imager_profile/public_profile.html'
    model = ImagerProfile

    def get_context_data(self, username=None):
        """Query applicable photo and album counts."""
        user = User.objects.get(username=username)
        return {'user': user}
