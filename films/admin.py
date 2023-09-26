from django.contrib import admin
from .models import Film, CriticComment, MemberComment


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'release_date')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CriticComment)
class CriticCommentAdmin(admin.ModelAdmin):

    list_display = ('film', 'critic')
    search_fields = ['film']


admin.site.register(MemberComment)
