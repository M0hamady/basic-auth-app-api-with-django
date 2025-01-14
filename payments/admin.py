from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'amount', 'payment_method', 'status', 'payment_date')
    list_filter = ('payment_method', 'status', 'payment_date')
    search_fields = ('subscription__user__username', 'subscription__service__name')
    ordering = ('-payment_date',)
