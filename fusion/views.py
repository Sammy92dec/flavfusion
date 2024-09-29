from django.shortcuts import render, HttpResponse
from . import models
recipes =[ {
    'author': 'kelly',
    'title': 'meatball sub',
    'directions': 'combine all ingredients',
    'date_posted': 'Sep 27, 2024',
},
{
    'author': 'Jusi',
    'title': 'vegi sub',
    'directions': 'combine all ingredients',
    'date_posted': 'Sep 28, 2024',
},
 {
    'author': 'Dom',
    'title': 'turkey sub',
    'directions': 'combine all ingredients',
    'date_posted': 'Sep 29, 2024',
},
]

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes' : recipes
        }
    return render(request, "recipes/home.html", context)

def about(request):
    context = {
        'title' : 'About'
        }
    return render(request, "recipes/about.html", context)