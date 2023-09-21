from django.shortcuts import render, get_object_or_404
from .models import Film


def Home(request, *args, **kwargs):
    """
    Renders the Home page
    """

    return render(
        request,
        "home.html",
        {
        },
    )


def FilmDetail(request, slug, *args, **kwargs):
    """
    Renders the Film Detail Page
    """

    queryset = Film.objects.all()
    film = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "film_detail.html",
        {
            "film": film
        }
    )