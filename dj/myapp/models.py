from django.db import models


class Person(models.Model):
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', "Female"),
    )
    age = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=100)
    mass = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, null=True, choices=SEX_TYPES)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"
