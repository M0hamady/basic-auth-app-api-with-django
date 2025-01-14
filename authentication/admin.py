from django.contrib import admin
from .models import CustomUser
from services.models import Service

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'service_request_status', 'requested_service')
    list_filter = ('service_request_status', 'requested_service')
    search_fields = ('username', 'email')
    ordering = ('username',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # يمكن إضافة تصفية إضافية إذا لزم الأمر
        return queryset

admin.site.register(CustomUser, CustomUserAdmin)
