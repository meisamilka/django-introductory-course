from email.policy import default
from django.db import models

# Create your models here.


class username(models.Model):

    fisrtname = models.CharField(
        max_length=50, verbose_name="name", default="")
    lastname = models.CharField(max_length=50, verbose_name="family")
    age = models.IntegerField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    count = models.BigIntegerField(null=True, blank=True)
    # count = models.SmallIntegerField(blank=True)
    price = models.FloatField(default=0.1)
    cost = models.DecimalField(default=0.1, max_digits=10, decimal_places=3)

    description = models.TextField(default="")
    status = models.BooleanField(default=False, null=True)

    # status = models.NullBooleanField(default=False)
    # registerdate = models.DateField(auto_now_add=True)
    # updatedate = models.DateTimeField(auto_now=True)

    # time = models.TimeField()
    # duration = models.DurationField()


class Teacher(models.Model):
    MALE = 0
    FEMALE = 1
    OTHER = 2

    GENDER_CHOICES = (
        (OTHER, "other"),
        (MALE, "male"),
        (FEMALE, "female")
    )

    name = models.CharField(
        max_length=50, db_column="firstname", db_comment="")
    family = models.CharField(max_length=50)
    teachercode = models.CharField(max_length=10)

    # gender = models.IntegerField(
    #     choices=GENDER_CHOICES)


class Person(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
