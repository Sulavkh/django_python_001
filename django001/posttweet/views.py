from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def posttweet(request):
    return render(request, 'posttweet.html')