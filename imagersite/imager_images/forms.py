"""Form for adding and editings photos/albums."""
from django import forms

from imager_images.models import Album, Photo


class PhotoForm(forms.ModelForm):
    """PhotoForm class to create new photos."""

    class Meta:
        """Meta subclass for PhotoForm."""

        model = Photo
        fields = ['title', 'imgfile', 'description', 'published']
        widgets = {'description': forms.Textarea()}


class AlbumForm(forms.ModelForm):
    """AlbumForm class to create new photos."""

    class Meta:
        """Meta subclass for AlbumForm."""

        model = Album
        fields = ['title', 'photo', 'description', 'cover', 'published']
        widgets = {'description': forms.Textarea()}
