from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ip_tracking.views import landing_page, login_view

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Backend Security API",
        default_version='v1',
        description="API documentation for ALX Backend Security",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),   # ✅ add this line

    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
