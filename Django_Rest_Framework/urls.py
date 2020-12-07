
from django.urls import path

from .views import (
    #apis
    apiIndexView, 
    CreateView, 
    createView,
    deleteView,
    DeleteView, 
    IndexView, 
    updateView, 
    UpdateView,
    handleLike,
    #template
    templateView
    )


urlpatterns = [
    path('', templateView, name="templateView"),


    path('class-index/', IndexView.as_view(), name="index"),
    path('index/', apiIndexView, name="index"),
    path('class-post/', CreateView.as_view(), name="post"),
    path('post/', createView, name="test-post"),
    path('update/<int:id>/', updateView, name="update"),
    path('class-update/<int:pk>/', UpdateView.as_view(), name="class-update"),
    path('delete/<int:id>/', deleteView, name="delete"),
    path('class-delete/<int:pk>/', DeleteView.as_view(), name="class-delete"),
    path('like/', handleLike, name="like"),
]
