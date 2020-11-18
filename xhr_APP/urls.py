
from django.urls import path

from .views import home_view, home_Api_View


urlpatterns = [
    path('', home_view),
    path('Api/', home_Api_View),
]
