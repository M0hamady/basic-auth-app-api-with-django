from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, ReportViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),  # Includes all the API routes
]
