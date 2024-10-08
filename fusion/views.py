from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from . import models



# Create your views here.

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
        }
    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe
    
class RecipeCreateView(CreateView):
    model =  models.Recipe
    fields = ['title','description']



def about(request):
    return render(request, "recipes/about.html", {'title':'about us page'})