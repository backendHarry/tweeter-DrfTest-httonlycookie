
from django.urls import path

from .views import templateView


urlpatterns = [
    path('register/', templateView, name="templateView"),
]
