from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weight(value):
    if value > 120:
        raise ValidationError(
            _('%(value)s kg! You are too fat bro'),
            params={'value': value},
        )


class Person(models.Model):
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', "Female"),
    )
    age = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=100)
    mass = models.IntegerField(blank=True, null=True, validators=[validate_weight])
    sex = models.CharField(max_length=10, null=True, choices=SEX_TYPES)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

    def calculate_calories(self):
    # jakie jest zapotrzebowanie kaloryczne dla danej osoby
        if self.sex == 'M':
            return 66.47 + 13.7 * float(self.mass) + 5 * float(self.height) - 6.76 *  float(self.age)
        else:
            return 655.1 + 9.567 * float(self.mass) + 1.85 * float(self.height) - 4.68 * float(self.age)
