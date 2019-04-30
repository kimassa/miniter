from django.db import models
from user.models import User

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
