import pytest
from blog.models import Post, Vote

def test_post_creation(post):
    assert post.title == "My First Post"
    assert post.hashtags.count() == 2

def test_vote_creation(vote):
    assert vote.value == Vote.UPVOTE

def test_comment_creation(comment):
    assert comment.body == "This is a comment on the first post."
