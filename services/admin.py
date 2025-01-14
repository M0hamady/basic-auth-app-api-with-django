from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_monthly', 'price_annual')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)
