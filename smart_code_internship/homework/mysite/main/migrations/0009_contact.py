# Generated by Django 4.2.3 on 2023-07-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact email')),
                ('phone', models.CharField(max_length=30, verbose_name='Contact phone')),
                ('subject', models.CharField(max_length=60, verbose_name='Contact subject')),
                ('message', models.TextField(verbose_name='Contact message')),
            ],
        ),
    ]
