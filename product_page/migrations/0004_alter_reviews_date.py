# Generated by Django 3.2.18 on 2023-03-27 03:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_page', '0003_alter_reviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
