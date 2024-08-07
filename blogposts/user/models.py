from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=120)




