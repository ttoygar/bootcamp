# Generated by Django 3.2.9 on 2021-12-03 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20211203_0625'),
        ('orders', '0002_alter_invoiceaddress_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceAddress',
            new_name='ShippingAddress',
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Shipping Address', 'verbose_name_plural': 'Shipping Addresses'},
        ),
    ]