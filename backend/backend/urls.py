from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ingredients.routers import router_ingredients
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from recipes.routers import router_recipes
from users.routers import router_users
from users.views import APILogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_ingredients.urls)),
    path('api/', include(router_recipes.urls)),
    path('api/', include(router_users.urls)),
    path('api/', include('djoser.urls')),
    path('api/auth/token/login/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/token/logout/', APILogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
