from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    author = forms.CharField(label='Author', max_length=100, required=True)
    content = forms.CharField(label='Content',widget=forms.Textarea, required=True)

    class Meta:
        model = Comment
        fields = ['author', 'content']
