# Generated by Django 5.1.4 on 2025-01-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price_fixed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
