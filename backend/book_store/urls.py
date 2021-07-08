from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # apps
    path('api-v1/',include('user.urls')),
    path('api-v1/',include('product.urls')),
    path('api-v1/',include('order.urls')), 
    path('api-v1/',include('shopcart.urls')),

    # admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # jwt
    path('api-v1/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # patterns
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # swagger docs
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]