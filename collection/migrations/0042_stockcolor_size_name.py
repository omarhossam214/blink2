# Generated by Django 3.2.18 on 2023-05-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0041_stockcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcolor',
            name='size_name',
            field=models.CharField(default='t', max_length=100),
            preserve_default=False,
        ),
    ]
