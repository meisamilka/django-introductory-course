
from django.contrib import admin
from django.urls import path

from post.views import save_person

urlpatterns = [
    path('save/', save_person),
]
