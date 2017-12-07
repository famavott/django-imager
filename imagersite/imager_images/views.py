"""Views for imager_images."""
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from imager_images.forms import AlbumForm, PhotoForm

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


class CreatePhoto(CreateView):
    """View to create photo."""

    template_name = 'imager_images/photo_form.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Validate if form submission successful."""
        form.instance.user = self.request.user.profile
        return super(CreatePhoto, self).form_valid(form)


class CreateAlbum(CreateView):
    """View to create album."""

    template_name = 'imager_images/album_form.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Validate if form submission successful."""
        form.instance.user = self.request.user.profile
        return super(CreateAlbum, self).form_valid(form)


class EditPhoto(UpdateView):
    """Edit existing photos."""

    template_name = 'imager_images/photo_edit.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Validate if form submission successful."""
        form.instance.user = self.request.user.profile
        return super(EditPhoto, self).form_valid(form)


class EditAlbum(UpdateView):
    """Edit existing albums."""

    template_name = 'imager_images/album_edit.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Validate if form submission successful."""
        form.instance.user = self.request.user.profile
        return super(EditAlbum, self).form_valid(form)
