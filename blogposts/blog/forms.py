from .models import Comment, Post, Hashtag
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
      
class PostForm(forms.ModelForm):
    hashtags = forms.CharField(required=False, help_text="Enter hashtags separated by commas")
    
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'links', 'slug', 'hashtags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'links': forms.TextInput(attrs={'placeholder': 'http://example.com, http://another-link.com'})
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        hashtags_str = self.cleaned_data['hashtags']
        hashtags_list = [ht.strip() for ht in hashtags_str.split(',')]
        if commit:
            instance.save()
        for tag in hashtags_list:
            hashtag, created = Hashtag.objects.get_or_create(name=tag)
            instance.hashtags.add(hashtag)
        return instance