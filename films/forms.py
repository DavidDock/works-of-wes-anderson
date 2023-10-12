from .models import MemberComment, Score
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = " add comment (max length - 300)"


class ScoreForm (forms.ModelForm):
    class Meta:
        model = Score
        fields = ('film', 'style', 'humour', 'story',)
