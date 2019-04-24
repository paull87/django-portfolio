from django.urls import path
from bootstrap import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("buttons/", views.buttons, name="buttons"),
    path("forms/", views.forms, name="forms"),
    path("navbar/", views.navbar, name="navbar"),
]

urlpatterns += staticfiles_urlpatterns()
