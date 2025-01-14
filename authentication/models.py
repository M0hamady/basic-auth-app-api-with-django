from django.contrib.auth.models import AbstractUser
from django.db import models
from services.models import Service  # استيراد النموذج الخاص بالخدمات

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    requested_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='requested_services')
    service_request_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    
    def __str__(self):
        return self.username
