
from django.urls import path

from .views import templateRegisterView, templateLoginView


urlpatterns = [
    path('register/', templateRegisterView, name="register"),
    path('login/', templateLoginView, name="login"),
]
