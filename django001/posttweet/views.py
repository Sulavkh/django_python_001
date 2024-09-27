from django.shortcuts import render, HttpResponse
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    Tweet.objects.all().order_by('-created_at')
    
def posttweet(request):
    return render(request, 'posttweet.html')

def contact(request):
    return render(request, 'contact.html')


