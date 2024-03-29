from django.utils.translation import gettext_lazy as _
from djoser.serializers import UserCreateSerializer
from recipes.serializers import RecipeFavoriteSerializer
from rest_framework import serializers

from .models import User, UserSubscription


class UserSerializer(UserCreateSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return UserSubscription.objects.filter(
            subscriber=user, subscription=obj
        ).exists()


class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='subscription.email')
    id = serializers.EmailField(source='subscription.id')
    username = serializers.EmailField(source='subscription.username')
    first_name = serializers.EmailField(source='subscription.first_name')
    last_name = serializers.EmailField(source='subscription.last_name')
    is_subscribed = serializers.SerializerMethodField(read_only=True)
    recipes_count = serializers.SerializerMethodField(read_only=True)
    recipes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserSubscription
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count',
        )

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return UserSubscription.objects.filter(
            subscriber=user, subscription=obj.subscription
        ).exists()

    def get_recipes_count(self, obj):
        return obj.subscription.recipes.count()

    def get_recipes(self, obj):
        recipes = obj.subscription.recipes.all()[:3]
        return RecipeFavoriteSerializer(recipes, many=True).data


class SubscriptionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = (
            'subscriber',
            'subscription',
        )

    def validate_subscription(self, value):
        request = self.context['request']
        if not request.user == value:
            return value
        raise serializers.ValidationError(
            _('Вы не можете подписаться на себя')
        )
