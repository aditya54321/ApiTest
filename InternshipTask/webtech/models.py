from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    rating = models.FloatField()
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    

