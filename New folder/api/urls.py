
from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet
from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
