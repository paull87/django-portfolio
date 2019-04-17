from django.urls import path
from testing_css import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.basics, name="basics"),
]

urlpatterns += staticfiles_urlpatterns()
