# Generated by Django 3.2.18 on 2023-05-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0083_auto_20230505_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1683319274.799316, max_length=100, null=True),
        ),
    ]