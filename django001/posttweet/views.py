from django.shortcuts import render, HttpResponse
from django.db import models
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    Tweet.objects.all().order_by('-created_at')
    
def posttweet(request):
    return render(request, 'posttweet.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        created_at = models.DateTimeField()
        contact = Contact(name=name, email=email, phone=phone, desc=desc, created_at=created_at)
        contact.save()
    return render(request, 'contact.html')


