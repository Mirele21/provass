from django.contrib import admin
from django.urls import include, path

urlpatterns = [
path("", include("polls.urls")),
path("", admin.site.urls),
]
