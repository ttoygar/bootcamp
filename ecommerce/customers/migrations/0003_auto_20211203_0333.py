# Generated by Django 3.2.9 on 2021-12-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_address_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=200, verbose_name='Line 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=200, verbose_name='Line 2'),
        ),
    ]