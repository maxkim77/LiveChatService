#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.createroom, name="createroom"),
    path("<str:room_name>/", views.chatroom, name="chatroom"),
]