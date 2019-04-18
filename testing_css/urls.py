from django.urls import path
from testing_css import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.basics, name="basics"),
    path("assessment_one/", views.assessment_one, name="assessment_one"),
    path("fonts/", views.fonts, name="fonts"),
    path("box_model/", views.box_model, name="box_model"),
]

urlpatterns += staticfiles_urlpatterns()
