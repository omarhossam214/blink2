# Generated by Django 3.2.18 on 2023-04-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0061_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1682521841.465103, max_length=100, null=True),
        ),
    ]