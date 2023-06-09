# Generated by Django 3.2.18 on 2023-05-08 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0045_alter_categories_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_num', models.IntegerField(blank=True, default=0, null=True)),
                ('products_num', models.IntegerField(blank=True, default=0, null=True)),
                ('first_slider_img', models.ImageField(null=True, upload_to='images')),
                ('second_slider_img', models.ImageField(null=True, upload_to='images')),
                ('third_slider_img', models.ImageField(null=True, upload_to='images')),
                ('promo_code_img', models.ImageField(null=True, upload_to='images')),
                ('best_seller_products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.products')),
            ],
        ),
    ]
