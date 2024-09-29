from django.db import models
from django.contrib.auth.models import User

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
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} Email: {self.email}"
