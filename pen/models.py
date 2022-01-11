from django.db import models

# Create your models here.
class Memo(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
