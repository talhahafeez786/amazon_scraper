from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 255)
    asin = models.CharField(max_length = 50, unique = True)
    sku = models.CharField(max_length = 50, blank = True, null = True)
    image_url =  models.URLField(blank = True, null = True)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, related_name = 'products')
    last_updated = models.DateTimeField(auto_now  = True)

    def __str__(self):
        return self.name

