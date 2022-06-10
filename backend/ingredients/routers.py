from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet


router_ingredients = DefaultRouter()
router_ingredients.register('ingredients', IngredientViewSet, basename='ingredients')
