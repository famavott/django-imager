"""Views for imager_images."""
from django.shortcuts import render

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


def album_view(request):
    """View for the user's albums."""
    user = request.user.profile
    albums = Album.objects.filter(user=user)
    return render(request, 'imager_images/albums.html',
                  context={'albums': albums})


def photos_view(request):
    """View for the user's photos."""
    user = request.user.profile
    photos = Photo.objects.filter(user=user)
    return render(request, 'imager_images/photos.html',
                  context={'photos': photos})


class PhotosView(ListView):
    """View all photos for a user."""

    template_name = 'imager_images/photos.html'
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        """."""
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
