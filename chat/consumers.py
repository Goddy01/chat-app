import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    # Asynchronous methods allow for non-blocking execution, meaning they can perform other tasks 
    # while waiting for certain operations to complete, 
    # such as waiting for I/O operations or network requests.
    async def connect(self):
        """Executes when a client establishes a websocket conn with the server"""
        # The scope(self.scope) is the place to get connection information and where middleware puts the attributes it wants to let you access
        # in the same way that Django's middleware adds things to request
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # JOIN ROOM GROUP
        await self.channel_layer.group_add(self.room_group_name, self.channel_name) # the await keyword waits for this line to finish before proceeding to the next line
        await self.accept() # sends a msg to the client indicating that the server has accepted the websocket conn, once the client receives this msg it can start sending and receiving msgs through the websocket connection

    async def disconnect(self):
        """To disconnect a connection"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)