from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name="fusion-home"),
    #path('about/', views.about, name="fusion-about"),
]
