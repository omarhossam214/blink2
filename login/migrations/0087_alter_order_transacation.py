# Generated by Django 3.2.18 on 2023-05-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0086_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1683320304.038132, max_length=100, null=True),
        ),
    ]
