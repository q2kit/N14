# Generated by Django 3.2.7 on 2021-11-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_image_product_img_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_capacity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productID', models.CharField(max_length=32)),
                ('capacity', models.CharField(max_length=10)),
            ],
        ),
    ]
