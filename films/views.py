from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    critic_comments = film.critic_comments.all()
    member_comments = film.member_comments.filter(
        approved=True).order_by("-created_on")

    return render(
        request,
        "film_detail.html",
        {
            "film": film,
            "critic_comments": critic_comments,
            "member_comments": member_comments
        }
    )


"""
login_required learnt from https://docs.djangoproject.com/en/4.2/topics/auth/default/
"""
@login_required
def MemberArea(request, *args, **kwargs):
    """
    Renders the Member Area page
    """

    return render(
        request,
        "member_area.html",
        {
        },
    )
