from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
