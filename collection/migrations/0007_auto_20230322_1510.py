# Generated by Django 3.2.18 on 2023-03-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AlterField(
            model_name='products',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.categories'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
