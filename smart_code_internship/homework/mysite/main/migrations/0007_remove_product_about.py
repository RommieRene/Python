# Generated by Django 4.2.3 on 2023-07-04 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='about',
        ),
    ]
