# Generated by Django 3.2.18 on 2023-05-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0081_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1682952022.650669, max_length=100, null=True),
        ),
    ]
