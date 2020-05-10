from django.db import models

# Create your models here.

class destination(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
