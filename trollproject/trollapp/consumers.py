# File routes the WebSocket connections to the consumers
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
# WebSocket Chat Code taken from https://www.geeksforgeeks.org/realtime-chat-app-using-django/ 
# modified to keep track of connected users, and also join using a socket id
class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connected_users = {} # use dictionary instead of a set

    async def connect(self):
        self.websocket_id = self.scope['url_route']['kwargs']['websocket_id']
        self.roomGroupName = f'chat_{self.websocket_id}'

        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

        if self.roomGroupName not in self.connected_users:
            self.connected_users[self.roomGroupName] = set()

        await self.update_connected_users(add_user=True)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

        # Send the list of the connected users
        await self.update_connected_users(add_user=False)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            }
        )

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "connected_users": list(self.connected_users[self.roomGroupName]),
        }))

    async def update_connected_users(self, add_user=True):
        if add_user:
            self.connected_users[self.roomGroupName].add(self.scope['user'].username)
        else:
            self.connected_users[self.roomGroupName].remove(self.scope['user'].username)

        await self.send_connected_users()

    async def send_connected_users(self):
        await self.send(text_data=json.dumps({
            "connected_users": list(self.connected_users[self.roomGroupName]),
        }))


# old code copy just in case I mess something up
'''
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.roomGroupName = "group_chat_gfg"

        self.websocket_id = self.scope['url_route']['kwargs']['websocket_id']
        self.roomGroupName = f'chat_{self.websocket_id}'

        # make a set to keep track of the connected users
        self.connected_users = set()

        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()

        # Send the list of the connected users
        await self.update_connected_users()

    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
        # when a user disconnects update the list
        await self.update_connected_users()
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            }
        )
    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({
            "message": message,
            "username": username,
            "connected_users": list(self.connected_users),  # connected users
        }))

    async def update_connected_users(self):
        group_channels = await self.channel_layer.group_channels(self.roomGroupName)
        self.connected_users = {channel.split('.')[-1] for channel in group_channels}

'''

