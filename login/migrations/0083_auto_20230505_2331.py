# Generated by Django 3.2.18 on 2023-05-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0082_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverage_area',
            name='city_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1683318709.163758, max_length=100, null=True),
        ),
    ]
