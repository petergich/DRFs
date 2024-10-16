from django.db import models

class category(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length=2000)
class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length= 30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    class Meta:
        ordering = ['price']  
        managed = True
        verbose_name = 'product'
        verbose_name_plural = 'products'

# Create your models here.
