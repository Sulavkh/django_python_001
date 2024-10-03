from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Contact
from django.contrib import messages
from django.utils import timezone
from django.db import DatabaseError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('posttweet:login')
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        # Check if the user entered an email and password
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('posttweet:loggedin')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('posttweet:login')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return render(request, 'posttweet:login')

def loggedin(request):
    return render(request, 'loggedin.html')

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
        
        if name and email and phone and desc:  # Basic form validation
            try:
                contact = Contact(
                    name=name,
                    email=email,
                    phone=phone,
                    desc=desc,
                    created_at=timezone.now()
                )
                contact.save()
                messages.success(request, "Thank you! Your Message has been sent")
                return redirect('posttweet:contact')  # Note the lowercase 'contact'
            except DatabaseError as e:
                messages.error(request, f"An error occurred: {str(e)}")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")
        else:
            messages.error(request, "Please fill all the fields")
    
    return render(request, 'contact.html')

