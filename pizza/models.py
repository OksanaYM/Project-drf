from django.db import models

# Create your models here.

class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizza'

    name = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.FloatField()

