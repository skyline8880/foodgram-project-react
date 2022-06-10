from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet, TagViewSet


router_recipes = DefaultRouter()
router_recipes.register('tags', TagViewSet, basename='tags')
router_recipes.register('recipes', RecipeViewSet, basename='ingredients')
