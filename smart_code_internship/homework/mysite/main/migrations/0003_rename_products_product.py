# Generated by Django 4.2.3 on 2023-07-03 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
