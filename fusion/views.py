from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    context = {
        'recipes' : recipes
        }
    return render(request, "recipes/home.html", context)

def about(request):
    context = {
        'title' : 'About'
        }
    return render(request, "recipes/about.html", context)