from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

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
    
    data_list = [i.serializer() for i in posts]
    data ={
        'data_list' : data_list
    }

    return JsonResponse(data)


def home_view(request):
    if(request.method == 'POST'):
        tweetForm = TweetForm(request.POST or None)
        if tweetForm.is_valid():
            obj=tweetForm.save(commit=False)
            obj.save()
            if request.is_ajax():
                return JsonResponse(obj.serialzer(), status=201)
    tweetForm = TweetForm()
    return render(request, 'xhr_APP/home.html', {})


def tweet_create_view(request):
    if(request.method == 'POST'):
        tweetForm = TweetForm(request.POST or None)
        if tweetForm.is_valid():
            obj = tweetForm.save(commit=False)
            obj.save()
            if request.is_ajax():
                return JsonResponse(obj.serializer(), status=201) #with this serializer method giving us access to Json containing our data, we can then use the 'appending to tweetList' which is more faster than reloading tweetList all the time
            return redirect('/xhr')
    tweetForm = TweetForm()
    return render(request, 'xhr_APP/create_form.html', {"tweetForm":tweetForm})
