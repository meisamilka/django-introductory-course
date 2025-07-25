from django.db import models
# from django.utils.text import slugify


# # Create your models here.


# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     national_code = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.name


# class Gender(models.TextChoices):
#     MALE = 'male', 'Male'
#     FEMALE = 'female', 'Female'
#     OTHER = 'other', 'Other'


# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True, blank=True)
#     password = models.CharField(max_length=100)
#     gender = models.CharField(
#         max_length=6, choices=Gender.choices, default=Gender.OTHER)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)


# class Gender(models.IntegerChoices):
#     MALE = 1, 'Male'
#     FEMALE = 2, 'Female'
#     OTHER = 3, 'Other'


# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True, blank=True)
#     password = models.CharField(max_length=100)
#     gender = models.IntegerField(choices=Gender.choices, default=Gender.OTHER)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True,
#                             editable=False, allow_unicode=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title, allow_unicode=True)
#         super().save(*args, **kwargs)


# jadadiftarin haye ai
# milka.com/jadadiftarin-haye-ai


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,
                            editable=False, allow_unicode=True)
    print_year = models.IntegerField()
    price = models.IntegerField()
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    publisher_id = models.BigIntegerField(default=0)
    author_id = models.BigIntegerField(default=0)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,
                            editable=False, allow_unicode=True)
    address = models.TextField()
    phone = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
