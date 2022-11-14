from django.urls import path
from . import views

app_name = "press"

urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("send-message/", views.send_message, name="send_message"),
]