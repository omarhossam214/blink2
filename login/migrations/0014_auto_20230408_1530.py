# Generated by Django 3.2.18 on 2023-04-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0020_products_data_order'),
        ('login', '0013_auto_20230408_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.products')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductSummary',
        ),
        migrations.AlterField(
            model_name='order',
            name='transacation',
            field=models.CharField(default=1680960648.819589, max_length=100, null=True),
        ),
    ]
