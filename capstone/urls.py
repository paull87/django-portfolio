from django.urls import path
from capstone import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.capstone_welcome, name="capstone_welcome"),
    path("thankyou/", views.capstone_thankyou, name="capstone_thankyou"),
]

urlpatterns += staticfiles_urlpatterns()
