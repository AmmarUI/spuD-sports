import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    CATEGORIES = [
        ('shoes', 'Shoes'),
        ('balls', 'Balls'),
        ('jerseys', 'Jerseys'),
        ('socks', 'Socks'),
        ('shorts', 'Shorts')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    stock = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(choices = CATEGORIES, default = 'balls')
    is_featured = models.BooleanField()
