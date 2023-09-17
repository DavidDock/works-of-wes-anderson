from django.contrib import admin
from .models import Film, CriticComment, MemberComment

admin.site.register(Film)

admin.site.register(CriticComment)

admin.site.register(MemberComment)
