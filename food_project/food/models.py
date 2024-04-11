from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price models.
    def __str__(self):
    		return self.name
