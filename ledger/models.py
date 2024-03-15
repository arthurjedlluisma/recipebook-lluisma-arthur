from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("ledger:ingredient", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Arthur Lluisma")
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    update_on = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredient"
    )
