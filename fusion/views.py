from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h2>Home is working</h2>")

def about(request):
    return HttpResponse("<h1>About!!</h1>")