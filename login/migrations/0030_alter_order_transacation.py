# Generated by Django 3.2.18 on 2023-04-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681408451.247858, max_length=100, null=True),
        ),
    ]
