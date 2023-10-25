from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    stock_count = models.IntegerField(default=0, help_text="How many of this product are in stock?")
    price = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(max_length=20, name="stock keeping unit", unique=True, null=True, blank=True)

class ProductImage(models.Model):
    def __str__(self):
        return self.image
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name="categories")