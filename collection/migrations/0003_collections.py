# Generated by Django 3.2.18 on 2023-03-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100)),
            ],
        ),
    ]
