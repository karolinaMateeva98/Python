from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'links']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'links': forms.TextInput(attrs={'placeholder': 'http://example.com, http://another-link.com'})
        }