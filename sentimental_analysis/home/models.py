from django.db import models

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=30,)
    description = models.CharField(max_length=500)
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Comment(models.Model): 
    comment = models.CharField(max_length=500)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment