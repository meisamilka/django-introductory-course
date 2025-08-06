from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
