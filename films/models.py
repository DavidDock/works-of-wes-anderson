from django.db import models
from django.contrib.auth.models import User
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

    def save(self, *args, **kwargs):
        data = BytesIO(self.poster.read())
        upload = cloudinary.uploader.upload(data, secure=True)
        self.poster = upload['secure_url']

        super().save(*args, **kwargs)


class CriticComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name="critic_comments")
    critic = models.CharField(max_length=50)
    content = models.TextField(max_length=300)

    def __str__(self):
        return f"Comment {self.content} by {self.critic}"


class MemberComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member_comments"
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name="member_comments")
    name = models.CharField(max_length=80)
    content = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
