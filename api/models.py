import time
from django.db import models
from datetime import date
from datetime import datetime
from django.utils import dateparse


class Birth(models.Model):
    date_event = models.DateTimeField()
    number = models.IntegerField()


class Animal(models.Model):
    GENDER = (
        ('FEMALE', 'F'),
        ('MALE', 'M')
    )
    weight = models.FloatField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)

    def age(self):
        today = date.today()
        time_from_birth_date = abs(today - dateparse.parse_date(self.birth_date))
        return time_from_birth_date.days

    class Meta:
        abstract = True


class Rabbit(Animal):
    RACES = (
        ('NEW ZELAND', 0),
        ('GIANT FLANDES', 1)
    )
    race = models.IntegerField(choices=RACES)
    cage = models.IntegerField()
    father = models.ForeignKey(
        'Rabbit',
        on_delete=models.CASCADE
    )
    mother = models.ForeignKey(
        'Rabbit',
        on_delete=models.CASCADE,
    )

