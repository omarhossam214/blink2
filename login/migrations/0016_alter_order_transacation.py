# Generated by Django 3.2.18 on 2023-04-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_alter_order_transacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681008455.645244, max_length=100, null=True),
        ),
    ]