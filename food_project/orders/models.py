from django.db import models
from food.models import Food
# Create your models here.
class Order(models.Model):
    customer = models.CharField(max_length=200, unique=True)
    total_price = models.SmallIntegerField()
    food = models.ManyToManyField(Food)

    def __str__(self):
    		return self.customer