
from django.urls import path

from .views import home_view, home_Api_View, tweet_create_view


urlpatterns = [
    path('', home_view),
    path('Api/', home_Api_View),
    path('create/', tweet_create_view)
]
