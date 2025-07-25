from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    national_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    age = models.IntegerField()
    teachercode = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return f"{self.name} {self.family}"


