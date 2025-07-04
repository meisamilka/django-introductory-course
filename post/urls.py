from django.urls import path
from post.views import ilkeController


urlpatterns = [
    path('ilka/', ilkeController),
]
