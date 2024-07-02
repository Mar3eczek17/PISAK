from django.db import models
from django.contrib.auth.models import User


class Memo(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.body


