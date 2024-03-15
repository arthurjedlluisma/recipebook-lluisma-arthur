from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Recipe


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe-detail.html"
    redirect_field_name = "/accounts/login"


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipes-list.html"
