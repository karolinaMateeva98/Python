from .models import Comment, Post, Hashtag
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
      
class PostForm(forms.ModelForm):
    hashtags = forms.ModelMultipleChoiceField(queryset=Hashtag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'links', 'slug', 'hashtags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'links': forms.TextInput(attrs={'placeholder': 'http://example.com, http://another-link.com'})
        }