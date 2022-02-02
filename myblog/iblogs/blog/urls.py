
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('blog/<slug:url>',detailpost),
    path('category/<slug:url>',category),
    path('about/',about),
  
]