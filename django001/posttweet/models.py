from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tweet_photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} tweeted: {self.text[:20]}..."
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} Email: {self.email} created at {self.created_at}"
