# Generated by Django 3.2.7 on 2021-11-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_product_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_capacity',
            name='capacity',
            field=models.CharField(max_length=30),
        ),
    ]
