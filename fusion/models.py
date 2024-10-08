from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    title = models.CharField(max_length=200)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_owner", null=True) 


    published_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
