from django.urls import path
from testing_html import views

urlpatterns = [
    path("", views.basics, name="basics"),
    path("lists/", views.lists, name="lists"),
]
