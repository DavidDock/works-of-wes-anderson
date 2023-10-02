from .models import MemberComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ('content',)
