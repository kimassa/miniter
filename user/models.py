from django.db import models


class User(models.Model):
    """docstring for Tweet."""
    user_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
