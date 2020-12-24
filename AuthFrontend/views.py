from django.shortcuts import render

# Create your views here.


def templateRegisterView(request, *args, **kwargs):
    return render(request, 'AuthFrontend/account_create.html')

def templateLoginView(request, *args, **kwargs):
    return render(request, 'AuthFrontend/account_login.html')