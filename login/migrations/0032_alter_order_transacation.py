# Generated by Django 3.2.18 on 2023-04-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0031_auto_20230414_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681508125.265004, max_length=100, null=True),
        ),
    ]
