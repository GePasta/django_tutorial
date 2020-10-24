from django.db import models


class Person(models.Model):
    age = models.IntegerField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50)
