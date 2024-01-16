from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField('Product name', max_length=(50))
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='main_images')

    def __str__(self):
        return self.name

class Cart(models.Model):

    product=models.ForeignKey(Product, on_delete=models.CASCADE)