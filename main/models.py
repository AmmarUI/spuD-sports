import uuid
from django.db import models

# Create your models here.
class Shop(models.Model):
    CATEGORIES = [
        ('shoes', 'Shoes'),
        ('balls', 'Balls'),
        ('jerseys', 'Jerseys'),
        ('socks', 'Socks'),
        ('shorts', 'Shorts')
    ]

    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(choices = CATEGORIES, default = 'balls')
    is_featured = models.BooleanField()