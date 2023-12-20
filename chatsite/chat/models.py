# chat/models.py

from django.db import models

class ChatMessage(models.Model):
    room_name = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_name}: {self.message[:50]}"