# Generated by Django 3.2.18 on 2023-04-16 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0039_auto_20230416_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_fee',
        ),
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681609945.232038, max_length=100, null=True),
        ),
    ]
