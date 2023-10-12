from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Avg
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
    Renders the Film Detail Page with films comments and average scores
    Takes in slug from url
    """

    queryset = Film.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    critic_comments = film.critic_comments.all()
    member_comments = film.member_comments.filter(
        approved=True).order_by("-created_on")
    average_style = Score.objects.filter(
        film=film).aggregate(Avg('style'))['style__avg']
    average_style = round(average_style)
    average_humour = Score.objects.filter(
        film=film).aggregate(Avg('humour'))['humour__avg']
    average_humour = round(average_humour)
    average_story = Score.objects.filter(
        film=film).aggregate(Avg('story'))['story__avg']
    average_story = round(average_story)

    return render(
        request,
        "film_detail.html",
        {
            "film": film,
            "critic_comments": critic_comments,
            "member_comments": member_comments,
            "average_style": average_style,
            "average_humour": average_humour,
            "average_story": average_story
        }
    )


"""
login_required learnt from
https://docs.djangoproject.com/en/4.2/topics/auth/default/
"""


@login_required
def member_area(request, *args, **kwargs):
    """
    Renders the Member Area page with all user comments, scores and forms
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
    Add comment view
    Takes in slug from url and data from form
    If valid adds comment
    Gives relevant message
    Returns to member area
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
            messages.success(
                request, "Your comment has been sent for approval")
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def delete_comment(request, slug, comment_id, *args, **kwargs):
    """
    View to delete comment
    Takes in slug and comment id from url
    If correct user it deletes comment
    Sends relevant message
    Returns to member area
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
    Edits comment view
    Takes slug and comment id from url
    Edits comment if valid and changes approved to false
    Sends relevant message
    Returns to member area
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating your comment, sorry.')

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def add_score(request, *args, **kwargs):
    """
    Add score view
    If method is post it gets form details
    Checks if user already has score for film
    Adds score if appropriate
    Sends relevant message
    Returns to member area
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
                    request, "Please delete your previous rating")
            else:
                new_score.save()
                messages.success(
                    request, "Your score has been added")
        else:
            score_form = ScoreForm()
    else:
        score_form = ScoreForm()

    return HttpResponseRedirect(reverse('member_area'))


@login_required
def delete_score(request, score_id, *args, **kwargs):
    """
    View to delete score
    Takes in score id from url
    Deletes score if its users score
    Returns to member page
    """
    score = Score.objects.filter(id=score_id).first()

    if score.user == request.user:
        score.delete()
        messages.add_message(request, messages.SUCCESS, 'Score deleted')
    else:
        messages.add_message(request, messages.ERROR,
                             "You can not delete someone else's score")

    return HttpResponseRedirect(reverse('member_area'))
