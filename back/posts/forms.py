from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 2,
    }))

    class Meta:
        model = Post
        fields = ('content', 'image')


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Add a comment',
        'rows': 2,
    }))

    class Meta:
        model = Comment
        fields = ('text',)
