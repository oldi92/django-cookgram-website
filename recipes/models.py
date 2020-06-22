from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    method = models.TextField()
    author = models.ForeignKey(User, null=True , on_delete = models.PROTECT)

    def __str__(self):
        return self.title
    

class Ingredients(models.Model):
    recipe_id = models.ForeignKey(Recipe,on_delete = models.CASCADE)
    ingredient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.recipe_id.title

class CookInfo(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    prep_time = models.CharField(max_length=100)
    serves = models.IntegerField(default=0)
    cook_time = models.CharField(max_length=100)

    def __str__(self):
        return self.recipe_id.title