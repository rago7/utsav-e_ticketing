from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('verify_user/<str:pk>', views.sample, name="verifier")
]