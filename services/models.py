from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('marketing', 'Marketing'),
        ('social_media', 'Social Media Management'),
        ('coding', 'Coding Portfolio'),
        ('app_development', 'App Development'),
        ('ecommerce', 'E-commerce Site'),
        ('custom_system', 'Custom System'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    price_fixed = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_semi_annual = models.DecimalField(max_digits=10, decimal_places=2)
    price_annual = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
