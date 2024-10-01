from django.urls import path
from . import views

'app/model_viewtype'
'fusion/recipes_detail.html'


urlpatterns = [
    path('', views.RecipeListView.as_view(), name="home-flav"),
    path('recipe/<int:pk>/',views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),

    path('about/', views.about, name="about-flav"),
]

