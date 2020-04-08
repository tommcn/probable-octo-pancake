from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('c/<str:q>', views.display_class, name="classDetail"),
    path('codes', views.codes, name="codes")
]