from django.urls import path

from .views import RegisterView


urlpatterns = [
    path('register/Api', RegisterView.as_view(), name="register-view"),
]