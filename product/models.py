from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="subs")
    title = models.CharField(max_length=150)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    categories = models.ManyToManyField(Category, null=True,blank=True,related_name="products")
    
    def __str__(self):
        return self.title
    
class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="informations")
    text = models.TextField()
    
    def __str__(self):
        return self.text[:30]
