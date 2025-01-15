from rest_framework.viewsets import ModelViewSet
from .models import Subscription, Report
from .serializers import SubscriptionSerializer, ReportSerializer

class SubscriptionViewSet(ModelViewSet):
    """
    API endpoint for managing subscriptions.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    # Optional: Customize filtering if needed
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user)
        return Subscription.objects.none()


class ReportViewSet(ModelViewSet):
    """
    API endpoint for managing reports.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
