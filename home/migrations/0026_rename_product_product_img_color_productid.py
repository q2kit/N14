# Generated by Django 3.2.9 on 2021-11-30 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_product_img_color_productid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_img_color',
            old_name='product',
            new_name='productID',
        ),
    ]