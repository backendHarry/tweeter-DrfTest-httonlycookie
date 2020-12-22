from django.shortcuts import render

# Create your views here.


def templateView(request, *args, **kwargs):
    return render(request, 'AuthFrontend/account_create.html')