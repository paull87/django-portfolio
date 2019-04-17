from django.urls import path
from testing_css import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.basics, name="basics"),
    path("assessment_one/", views.assessment_one, name="assessment_one"),
]

urlpatterns += staticfiles_urlpatterns()
