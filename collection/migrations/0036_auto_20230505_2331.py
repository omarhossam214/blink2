# Generated by Django 3.2.18 on 2023-05-05 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0035_products_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='fabric',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='products',
            name='stock_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.stock_color'),
        ),
    ]