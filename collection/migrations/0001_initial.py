# Generated by Django 3.2.18 on 2023-03-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('describtion', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.BooleanField(default=True)),
            ],
        ),
    ]
