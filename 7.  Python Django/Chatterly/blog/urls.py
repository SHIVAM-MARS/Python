
from django.urls import path
from . import views

urlpatterns = [

    #render 
    path('home/', views.home),

    path('about/', views.about),

    path('contact/', views.contact)
]
