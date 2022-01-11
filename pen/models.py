from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memo(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
