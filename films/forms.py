from .models import MemberComment, Score
from django import forms

# Comment form


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ('film', 'content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = " add comment (max length - 250)"

# Score form


class ScoreForm (forms.ModelForm):
    class Meta:
        model = Score
        fields = ('movie', 'style', 'humour', 'story',)
