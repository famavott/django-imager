"""Views for imagersite."""
from django.http import HttpResponse

from django.template import loader

from django.shortcuts import render


def home_view(request):
    """View for the home page."""
    return render(request, '')
