# Generated by Django 3.2.18 on 2023-03-22 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0012_products_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_img',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.products')),
            ],
        ),
    ]