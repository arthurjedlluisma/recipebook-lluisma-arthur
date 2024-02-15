from django.urls import path

from .views import recipe_1, recipe_2, recipes_list

urlpatterns = [
    path("list", recipes_list, name="list"),
    path("1", recipe_1, name="1"),
    path("2", recipe_2, name="2"),
]

app_name = "ledger"
