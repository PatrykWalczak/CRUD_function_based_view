from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
