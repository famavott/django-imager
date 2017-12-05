"""Views for imagersite."""
from django.views.generic import TemplateView

from imager_images.models import Photo


class HomeView(TemplateView):
    """Class view for home page."""

    template_name = 'imagersite/home.html'

    def get_context_data(self):
        """Return random photo for home page."""
        photo = Photo.objects.order_by('?').first()
        return {'photo': photo}
