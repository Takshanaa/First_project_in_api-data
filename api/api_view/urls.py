from django.contrib import admin
from django.urls import path, include
from api_view import views

urlpatterns = [
    path("a1/", views.home, name="api_data"),
    path("a2/", views.chart, name="chart"),
]