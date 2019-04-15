from django.urls import path
from testing_html import views

urlpatterns = [
    path("", views.basics, name="basics"),
    path("lists/", views.lists, name="lists"),
    path("divspans/", views.div_spans, name="divs_spans"),
]
