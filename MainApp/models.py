from django.db import models
class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
