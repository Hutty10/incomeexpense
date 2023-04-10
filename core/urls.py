from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("user.urls", namespace="user")),
    path("income/", include("income.urls", namespace="income")),
]
