"""Views for imagersite."""
from django.shortcuts import render

from django.template import loader


def home_view(request):
    """View for the home page."""
    return render(request, 'imagersite/home.html')
