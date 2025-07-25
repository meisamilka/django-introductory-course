from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    national_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Gender(models.IntegerChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'
    OTHER = 'other', 'Other'


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=6, choices=Gender.choices, default=Gender.OTHER)
    last_updated = models.DateTimeField(auto_now=True, editable=False)




# class Gender(models.IntegerChoices):
#     MALE = 1, 'Male'
#     FEMALE = 2, 'Female'
#     OTHER = 3, 'Other'


# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True, blank=True)
#     password = models.CharField(max_length=100)
#     gender = models.IntegerField(choices=Gender.choices, default=Gender.OTHER)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
