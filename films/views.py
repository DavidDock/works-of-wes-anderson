from django.shortcuts import render


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
