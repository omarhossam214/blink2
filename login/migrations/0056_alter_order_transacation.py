# Generated by Django 3.2.18 on 2023-04-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0055_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1682453501.556675, max_length=100, null=True),
        ),
    ]
