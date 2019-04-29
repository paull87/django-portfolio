from django.urls import path
from javascript import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("runner/", views.runner, name="runner"),
    path("exercise3/", views.js_exercise3, name="js_exercise3"),
]

urlpatterns += staticfiles_urlpatterns()
