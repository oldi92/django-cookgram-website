from django.db import models

# Create your models here.


class VegetablesIngridients(models.Model):
    vegetables_ingredient = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.vegetables_ingredient


class MeatIngridients(models.Model):
    meat_ingredient = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.meat_ingredient


class OtherIngridients(models.Model):
    other_ingredient = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.other_ingredient
