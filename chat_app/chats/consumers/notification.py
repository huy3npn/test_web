import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
# from channels.generic.websocket import AsyncJsonWebsocketConsumer
from chats.models import Profile
from django.contrib.auth.models import User
class NewUserConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        # print("+"+self.room_name1)
        # self.room_name = 'new_user'
        self.room_group_name = 'notification'

        async_to_sync (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        aaa=User
        self.update_user_status(self.room_name,True,aaa)
        
        aa=Profile.objects.filter(online=True)
        print("nay la luc dau vao")
        print((aa))
        bb=""
        for i in aa:
            bb+=str(i)+","

        async_to_sync(self.channel_layer.group_send)(
             f'notification', {
                'type': 'new_messagechat',
                'message': bb[0:-1]
            }
        )
        print('connected  notiii !!!')

    def receive(self, text_data):
        print("vao ham receive noti ")
        async_to_sync (self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'new_user_notification',
                'message': "llll"
            }
        )

        print("da doc"+str(text_data))

    def new_user_notification(self, event):
        message = event['message']
        # message.online=False
        print("ssssss"+str(message))
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'new_user'
        }))

    def user_online(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'status_change'
        }))

    def disconnect(self, text_data):
        
        aaa=User
        user = self.scope['url_route']['kwargs']['username']
        self.update_user_status(user,False,aaa)
        aa=Profile.objects.filter(online=True)
        print("nay la luc cuoi")
        print((aa))
        bb=""
        for i in aa:
            bb+=str(i)+","
        async_to_sync(self.channel_layer.group_send)(
             f'notification', {
                'type': 'new_messagechat',
                'message': bb[0:-1]
            }
        )
        print("disconect noti")
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    def new_messagechat(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'online': True,
            "user":str(message)
            
        }))
 
    
    def update_user_status(self, userne,status,aaa):
        print(f"thay doi trang thai {status} ")
        a=User.objects.filter(username=userne).first()
        print(a)
        return Profile.objects.filter(user=a).update(online=status)
