from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

import cloudinary.uploader
from io import BytesIO

# Film Model


class Film(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    poster = CloudinaryField('image')
    sypnosis = models.TextField(max_length=400)
    trailer = models.URLField(max_length=100)
    info_link = models.URLField(max_length=100)
    color_class = models.CharField(max_length=20, blank=True)
    first_icon = CloudinaryField('icon', default='placeholder')
    second_icon = CloudinaryField('icon', default='placeholder')

    class Meta:
        ordering = ["-release_date"]

    def __str__(self):
        return self.title

# Critic Comments Model


class CriticComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name="critic_comments")
    critic = models.CharField(max_length=50)
    content = models.TextField(max_length=250)

    def __str__(self):
        return f"Comment {self.content} by {self.critic}"

# Critic Comments Model


class MemberComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member_comments"
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name="member_comments")
    name = models.CharField(max_length=80)
    content = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.name}"

# Score Model


class Score(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="scores")
    movie = models.ForeignKey(Film, on_delete=models.CASCADE,
                              related_name="scores")
    created_on = models.DateTimeField(auto_now_add=True)
    rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    style = models.IntegerField(choices=rating, default=5, validators=[
                                MinValueValidator(1), MaxValueValidator(5)])
    humour = models.IntegerField(choices=rating, default=5, validators=[
                                 MinValueValidator(1), MaxValueValidator(5)])
    story = models.IntegerField(choices=rating, default=5, validators=[
                                MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Score"
