"""Views for imager_images."""
from django.views.generic import DetailView, ListView, TemplateView

from imager_images.models import Album, Photo


class LibraryView(TemplateView):
    """View for library view."""

    template_name = "imager_images/library.html"

    def get_context_data(self, **kwargs):
        """Return album and photos for requested user."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        user = self.request.user.profile
        context['photos'] = user.photo.all()
        context['albums'] = user.album.all()
        return context


class AlbumsView(ListView):
    """View for the user's albums."""

    template_name = 'imager_images/albums.html'
    model = Album
    context_object_name = 'albums'

    def get_queryset(self):
        """Overwrite queryset to get all albums."""
        user = self.request.user.profile
        return user.album.all()


class PhotosView(ListView):
    """View all photos for a user."""

    template_name = 'imager_images/photos.html'
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        """Overwrite queryset to get all photos."""
        user = self.request.user.profile
        return user.photo.all()


class AlbumInfo(DetailView):
    """View for specific photo info."""

    template_name = 'imager_images/album_info.html'
    model = Album


class PhotoInfo(DetailView):
    """View for specific photo info."""

    template_name = 'imager_images/photo_info.html'
    model = Photo
