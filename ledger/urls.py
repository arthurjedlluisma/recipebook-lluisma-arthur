from django.urls import path

from .views import recipe_one, recipe_two, recipes_list

urlpatterns = [
    path("recipes/list", recipes_list, name="recipes_list"),
    path("recipe/1", recipe_one, name="recipe_one"),
    path("recipe/2", recipe_two, name="recipe_two"),
]

app_name = "ledger"
