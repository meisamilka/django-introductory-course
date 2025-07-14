from django.http import HttpResponse
from django.shortcuts import render

from post.models import Person

# Create your views here.


def save_person(request):

    # save

    # inst = Person(name="meisam", family="ilka")
    # inst.save()


    # Person.objects.create(name="meisam", family="ilka")

    # inst = Person(name="meisam", family="ilka")
    # inst.save()
    # inst.delete()

    return HttpResponse("ok ;)")
