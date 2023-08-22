from django.db import models



class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    thumbnail = models.URLField()
    images = models.ManyToManyField('ProductImage', related_name='productImages')
    
    
    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        image_url = models.URLField()

        def __str__(self):
            return f"Image for {self.product.name}"


