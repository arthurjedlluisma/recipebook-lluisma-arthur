from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,
    ]


admin.site.register(Recipe, RecipeIngredientAdmin)
