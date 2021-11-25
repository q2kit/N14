# Generated by Django 3.2.8 on 2021-11-20 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211119_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Huyen',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tinh',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.CreateModel(
            name='Xa',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('huyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.huyen')),
            ],
        ),
        migrations.AddField(
            model_name='huyen',
            name='tinh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tinh'),
        ),
        migrations.AddField(
            model_name='customer',
            name='huyen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.huyen'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tinh',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tinh'),
        ),
        migrations.AddField(
            model_name='customer',
            name='xa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.xa'),
        ),
    ]