# Generated by Django 3.2.18 on 2023-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_auto_20230413_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681365516.299395, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large')], max_length=3),
        ),
    ]