from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField('Category name', max_length=(50))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ="Category"
        verbose_name_plural= 'Categories'

class Product(models.Model):
     
     category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='cat_prod')
     name = models.CharField('Product name', max_length=(60))
     price = models.PositiveIntegerField('Product price')
     img = models.ImageField('Product image', upload_to='images')
     slug = models.SlugField('Product slug', unique=True)
     date = models.DateTimeField(auto_now=True)
     about = models.TextField('About Product')
     def __str__(self):
        return self.name
    
     class Meta:
        ordering = ['-date'] 


class Contact(models.Model):
    email=models.EmailField('Contact email')
    phone=models.CharField('Contact phone', max_length=30)
    subject=models.CharField('Contact subject', max_length=60)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.email





