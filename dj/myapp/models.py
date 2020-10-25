from django.db import models


class Person(models.Model):
    age = models.IntegerField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"
