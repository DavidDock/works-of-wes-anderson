from django.shortcuts import render
from .models import Film


def home(request, *args, **kwargs):
    """
    Renders the Home page
    """

    return render(
        request,
        "home.html",
        {
        },
    )
