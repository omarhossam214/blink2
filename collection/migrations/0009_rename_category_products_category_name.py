# Generated by Django 3.2.18 on 2023-03-22 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_auto_20230322_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Category',
            new_name='Category_name',
        ),
    ]
