# Generated by Django 3.2.18 on 2023-05-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0042_stockcolor_size_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcolor',
            name='avail',
            field=models.BooleanField(default=False),
        ),
    ]