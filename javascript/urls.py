from django.urls import path
from javascript import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("runner/", views.runner, name="runner"),
    path("exercise3/", views.js_exercise3, name="js_exercise3"),
    path("project_one/", views.project_one, name="project_one"),
    path("arrays/", views.arrays, name="arrays"),
]

urlpatterns += staticfiles_urlpatterns()
