from django.views import generic
from .models import Post
from .forms import CommentForm, PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home') 
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    links = post.links.split(',') if post.links else []
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'links': links})

def upvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.upvotes += 1
    post.save()
    return redirect('post_detail', slug=post.slug)

def downvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.downvotes += 1
    post.save()
    return redirect('post_detail', slug=post.slug)