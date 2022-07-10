from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from djoser import views as djoser_views
from ingredients.routers import router_ingredients
from recipes.routers import router_recipes
from users.routers import router_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_ingredients.urls)),
    path('api/', include(router_recipes.urls)),
    path('api/', include(router_users.urls)),
    path('api/', include('djoser.urls')),
    path(
        'api/auth/token/login/',
        djoser_views.TokenCreateView.as_view(),
        name='login'
    ),
    path(
        'api/auth/token/logout/',
        djoser_views.TokenDestroyView.as_view(),
        name='login'
    ),
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
