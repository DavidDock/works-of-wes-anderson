from .models import MemberComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
        self.fields['content'].widget.attrs.update({
            'aria-label': 'Enter a comment'
        })
