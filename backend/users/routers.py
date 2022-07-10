from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, SubscriptionViewSet

router_users = DefaultRouter()
router_users.register(
    'users/subscriptions',
    SubscriptionViewSet,
    basename='subscriptions'
)
router_users.register('users', CustomUserViewSet, basename='custom-users')
