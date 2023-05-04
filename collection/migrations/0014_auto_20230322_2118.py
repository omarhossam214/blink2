# Generated by Django 3.2.18 on 2023-03-22 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0013_auto_20230322_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='collection.products')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
