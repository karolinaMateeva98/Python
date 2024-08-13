import pytest
from django.utils import timezone
from user.models import BlogUser
from blog.models import Hashtag, Post, Vote, Comment
from rest_framework.test import APIClient

@pytest.fixture
def blog_user(db):
    user = BlogUser.objects.create_user(username="testuser", email="testuser@example.com", password="password123")
    return user

@pytest.fixture
def hashtag_django(db):
    return Hashtag.objects.create(name="Django")

@pytest.fixture
def hashtag_python(db):
    return Hashtag.objects.create(name="Python")

@pytest.fixture
def post(db, blog_user, hashtag_django, hashtag_python):
    post = Post.objects.create(
        title="My First Post",
        slug="my-first-post",
        author=blog_user,
        updated_on=timezone.now(),
        content="This is the content of my first post.",
        created_on=timezone.now(),
        links="https://example.com, https://another-example.com"
    )
    post.hashtags.add(hashtag_django, hashtag_python)
    return post

@pytest.fixture
def vote(db, blog_user, post):
    return Vote.objects.create(user=blog_user, post=post, value=Vote.UPVOTE)

@pytest.fixture
def comment(db, blog_user, post):
    return Comment.objects.create(
        post=post,
        author=blog_user,
        body="This is a comment on the first post.",
        created_on=timezone.now()
    )

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }

@pytest.fixture
def create_user(db, user_data):
    return BlogUser.objects.create_user(**user_data)

@pytest.fixture
def client():
    return APIClient()