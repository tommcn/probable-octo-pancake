from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'codes'

urlpatterns = [
    path('', views.index, name="index"),
    path('c/<str:q>', views.display_class, name="classDetail"),
    path('codes', views.codes, name="codes"),
    path('soumission', views.soumission, name="soumission"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('classes/', views.user_classes, name="classes")
]