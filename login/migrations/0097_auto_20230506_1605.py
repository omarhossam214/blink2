# Generated by Django 3.2.18 on 2023-05-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0096_alter_order_transacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='selectedcolor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='selectedsize',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1683378307.636762, max_length=100, null=True),
        ),
    ]
