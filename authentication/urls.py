from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ForgotPasswordViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'auth', ForgotPasswordViewSet, basename='forgot-password')


urlpatterns = [
    path('', include(router.urls)),

]
