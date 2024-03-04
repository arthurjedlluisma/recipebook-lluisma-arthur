from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe-detail.html"


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes-list.html"
