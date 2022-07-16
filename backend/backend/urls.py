from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ingredients.routers import router_ingredients
from recipes.routers import router_recipes
from users.routers import router_users
from users.views import APILogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_ingredients.urls)),
    path('api/', include(router_recipes.urls)),
    path('api/', include(router_users.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/jwt/logout/', APILogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
