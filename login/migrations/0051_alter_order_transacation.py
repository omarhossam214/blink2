# Generated by Django 3.2.18 on 2023-04-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0050_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681853331.134931, max_length=100, null=True),
        ),
    ]
