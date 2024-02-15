from django.urls import path

from .views import recipe_1, recipe_2, recipes_list

urlpatterns = [
    path("recipes/list", recipes_list, name="list"),
    path("recipe/1", recipe_1, name="1"),
    path("recipe/2", recipe_2, name="2"),
]

app_name = "ledger"
