# Generated by Django 4.2.4 on 2023-08-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Product name')),
                ('price', models.PositiveBigIntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='main_images', verbose_name='Product image')),
            ],
        ),
    ]