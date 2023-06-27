from django.contrib import admin
from django.urls import path, include
from api_view import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api_view.urls"))
]
