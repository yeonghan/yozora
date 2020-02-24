from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    author = forms.CharField(
            label='Author', max_length=100, required=True,
            widget=forms.TextInput(attrs={'class': 'form-control'})
            )
    content = forms.CharField(
            label='Content', required=True,
            widget=forms.Textarea(attrs={'class': 'form-control'})
            )
    class Meta:
        model = Comment
        fields = ['author', 'content']
