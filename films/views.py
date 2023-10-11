from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Film, Score
from .forms import CommentForm, ScoreForm
from django.contrib import messages


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


def film_detail(request, slug, *args, **kwargs):
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
login_required learnt from
https://docs.djangoproject.com/en/4.2/topics/auth/default/
"""


@login_required
def member_area(request, *args, **kwargs):
    """
    Renders the Member Area page
    """
    all_comments = request.user.member_comments.all()
    all_scores = request.user.scores.all()

    return render(
        request,
        "member_area.html",
        {
            "all_comments": all_comments,
            "all_scores": all_scores,
            "comment_form": CommentForm(),
            "score_form": ScoreForm()
        },
    )


@login_required
def add_comment(request, slug, *args, **kwargs):
    """
    Adds comment
    """

    if request.method == "POST":

        queryset = Film.objects.all()
        film = get_object_or_404(queryset, slug=slug)
        user = request.user

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = user
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.film = film
            comment.save()
            messages.success(request, "Your comment has been sent for approval")
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def delete_comment(request, slug, comment_id, *args, **kwargs):
    """
    view to delete comment
    """
    queryset = Film.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    comment = film.member_comments.filter(id=comment_id).first()

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted')
    else:
        messages.add_message(request, messages.ERROR,
                             "You can not delete someone else's comment")

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def edit_comment(request, slug, comment_id, *args, **kwargs):
    """
    Edits comment
    """

    if request.method == "POST":

        queryset = Film.objects.all()
        film = get_object_or_404(queryset, slug=slug)
        comment = film.member_comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.film = film
            comment.approved = False
            comment.save()
            messages.success(
                request, "Your comment has been updated and sent for approval")
        else:
            messages.add(request, message.ERROR, 'Error updating your comment, sorry.')

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def add_score(request, *args, **kwargs):
    """
    Adds score
    """

    if request.method == "POST":

        user = request.user

        score_form = ScoreForm(data=request.POST)
        if score_form.is_valid():
            score_form.instance.user = user
            new_score = score_form.save(commit=False)
            film = new_score.film
            if Score.objects.filter(film=film, user=user).exists():
                messages.error(
                    request, "Please delete your previous rating for this film first")
            else:
                new_score.save()
                messages.success(
                    request, "Your score has been added")
        else:
            score_form = ScoreForm()
    else:
        score_form = ScoreForm()

    return HttpResponseRedirect(reverse('member_area'))
