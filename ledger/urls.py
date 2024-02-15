from django.urls import path

from .views import recipe_1, recipe_2, recipes_list

urlpatters = [
    path("list", recipes_list.html, name="list"),
    path("1", recipe_1.html, name="1"),
    path("2", recipe_2.html, name="2"),
]

app_name = "ledger"
