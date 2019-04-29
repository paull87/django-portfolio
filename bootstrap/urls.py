from django.urls import path
from bootstrap import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("buttons/", views.buttons, name="buttons"),
    path("forms/", views.forms, name="forms"),
    path("navbar/", views.navbar, name="navbar"),
    path("project/", views.project, name="project"),
    path("project_copy/", views.project_copy, name="project_copy"),
    path("project_signup/", views.project_signup, name="project_signup"),
]

urlpatterns += staticfiles_urlpatterns()
