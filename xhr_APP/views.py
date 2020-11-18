from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# models 
from .models import TweetPost

# forms
from .forms import TweetForm

# Create your views here.

def home_Api_View(request):
    posts = TweetPost.objects.all()
    '''since i'm using js as frontend i will love to bring my data as Json object..
       look like 
       [
            {1: post1},...
        ]
    '''
    
    data_list = [{'id': i.id, 'post':i.post, 'like':i.like} for i in posts]
    data ={
        'data_list' : data_list
    }

    return JsonResponse(data)


def home_view(request):
    if(request.method == 'POST'):
        tweetForm = TweetForm(request.POST or None)
        if tweetForm.is_valid():
            tweetForm.save(commit=False)
            tweetForm.save()
    tweetForm = TweetForm()
    return render(request, 'xhr_APP/home.html', {})

