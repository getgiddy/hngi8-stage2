from django.urls import path

from .views import home, send_email

urlpatterns = [
    path("", home, name="home"),
    path("send_email/", send_email, name="send_email")
]
