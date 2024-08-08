from django.db import models
from user.models import BlogUser


class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(BlogUser, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    links = models.TextField(blank=True, help_text="Add one or more links, separated by commas.")
    hashtags = models.ManyToManyField(Hashtag, related_name="posts", blank=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    @property
    def upvotes(self):
        return self.votes.filter(value=1).count()

    @property
    def downvotes(self):
        return self.votes.filter(value=-1).count()

    @property
    def total_votes(self):
        return self.upvotes + self.downvotes
    
class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )

    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'post')
        
    def __str__(self):
        return f'{self.post.title}'
    
    def save(self, *args, **kwargs):
        voted = Vote.objects.filter(user=self.user, post=self.post)
        if voted.exists():
            voted.delete()
        super().save(*args, **kwargs)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author.username)