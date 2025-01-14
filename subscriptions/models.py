from django.db import models
from authentication.models import CustomUser
from services.models import Service

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('expired', 'Expired'), ('suspended', 'Suspended')],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"


class Report(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.JSONField()  # لتخزين بيانات الإحصائيات
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
