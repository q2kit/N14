# Generated by Django 3.2.7 on 2021-11-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_product_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.FloatField(null=True),
        ),
    ]
