from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Post

@shared_task
def delete_old_posts():
    one_year_ago = timezone.now() - timedelta(days=365)
    old_posts = Post.objects.filter(created_on__lt=one_year_ago, comments__isnull=True)
    deleted_count, _ = old_posts.delete()
    return f"Deleted {deleted_count} old posts without comments."
