from django.shortcuts import render
from .models import ChatMessage


def createroom(request):
    return render(request, "chat/createroom.html")


def chatroom(request, room_name):
    last_messages = get_last_messages(room_name)
    return render(
        request,
        "chat/chatroom.html",
        {"room_name": room_name, "last_messages": last_messages},
    )

def get_last_messages(room_name):
    return ChatMessage.objects.filter(room_name=room_name).order_by("-timestamp")[:50]