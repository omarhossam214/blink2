# Generated by Django 3.2.18 on 2023-04-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0063_auto_20230426_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1682522157.421691, max_length=100, null=True),
        ),
    ]
