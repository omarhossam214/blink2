# Generated by Django 3.2.18 on 2023-04-28 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0028_auto_20230428_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocode',
            old_name='dis_img',
            new_name='image',
        ),
    ]
