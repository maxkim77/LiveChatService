#views.py
from django.shortcuts import render
from .models import ChatMessage


def createroom(request):
    chat_rooms = ChatMessage.objects.values('room_name').distinct()  # 중복되지 않는 방 이름 가져오기
    return render(request, "chat/createroom.html", {"chat_rooms": chat_rooms})

def chatroom(request, room_name):
    last_messages = get_last_messages(room_name)
    return render(
        request,
        "chat/chatroom.html",
        {"room_name": room_name, "last_messages": last_messages},
    )

def get_last_messages(room_name):
    return ChatMessage.objects.filter(room_name=room_name).order_by("-timestamp")[:50]