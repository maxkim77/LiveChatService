import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connect")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        print(self.room_name)
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        print("disconnect")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        print("receive")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

        await self.store_message(self.room_name, message)  # 추가

    async def chat_message(self, event):
        print("chat_message")
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async  # 추가
    def store_message(self, room_name, message):
        ChatMessage.objects.create(room_name=room_name, message=message)