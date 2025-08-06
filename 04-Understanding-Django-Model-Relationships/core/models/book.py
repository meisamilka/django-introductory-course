from django.db import models
from core.models.publisher import Publisher


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    print_year = models.IntegerField()

    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, related_name='books')

    # PROTECT
    # CASCADE
    # SET_NULLs
    # SET_DEFAULT
    # DO_NOTHING

    def __str__(self):
        return self.title


# pub.book_set.all()
# pub.books.all()
