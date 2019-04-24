from django.urls import path
from bootstrap import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("buttons", views.buttons, name="buttons"),
]

urlpatterns += staticfiles_urlpatterns()
