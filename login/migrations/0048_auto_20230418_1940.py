# Generated by Django 3.2.18 on 2023-04-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0047_alter_order_transacation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1681839631.104001, max_length=100, null=True),
        ),
    ]
