# Generated by Django 3.2.18 on 2023-03-22 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_rename_category_products_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Category_name',
            new_name='Category',
        ),
    ]