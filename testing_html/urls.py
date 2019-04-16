from django.urls import path
from testing_html import views

urlpatterns = [
    path("", views.basics, name="basics"),
    path("lists/", views.lists, name="lists"),
    path("divspans/", views.div_spans, name="divs_spans"),
    path("attributes/", views.attributes, name="attributes"),
    path("assessment_one/", views.level_one_assessment, name="assessment_one"),
]
