


# File routes the WebSocket connections to the consumers
import json
from channels.generic.websocket import AsyncWebsocketConsumer
 
# WebSocket Chat Code taken from https://www.geeksforgeeks.org/realtime-chat-app-using-django/ 
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.roomGroupName = "group_chat_gfg"

        self.websocket_id = self.scope['url_route']['kwargs']['websocket_id']
        self.roomGroupName = f'chat_{self.websocket_id}'


        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
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
            "message":message ,"username":username
        }))

