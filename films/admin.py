from django.contrib import admin
from .models import Film, CriticComment, MemberComment, Score

# Admin display for models


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'release_date')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CriticComment)
class CriticCommentAdmin(admin.ModelAdmin):

    list_display = ('film', 'critic')
    search_fields = ['film']


@admin.register(MemberComment)
class MemberCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'film', 'created_on', 'approved', 'id')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'film')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):

    list_display = ('movie', 'user')
    search_fields = ['movie']
