import datetime

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.expressions import F

from channels.db import database_sync_to_async
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer

from apps.chat.models import ChatRoomModel, MessageModel

UserModel = get_user_model()
class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room = None
        self.user_name = None

    async def connect(self):
        if not self.scope['user']:
            return await self.close()
        await self.accept()
        room_name = self.scope['url_route']['kwargs']['room']
        self.room, _ = await ChatRoomModel.objects.aget_or_create(name=room_name)
        self.user_name = await self.get_profile_name()
        await self.channel_layer.group_add(
            f'user_{self.scope['user'].id}',
            self.channel_name
        )
        await self.channel_layer.group_add(
            self.room.name,
            self.channel_name
        )
        messages = await self.get_last_five_messages()
        for name, text in messages:
            await self.sender({
                'message': text,
                'user': f'{name}',
                'request_id': str(datetime.datetime.now())
            })
        await self.channel_layer.group_send(
            self.room.name,
            {
                'type': 'sender',
                'message': f'{self.scope['user'].id}_{self.user_name} connected to chat'
            }
        )
    async def sender(self, data):
        await self.send_json(data)

    @action()
    async def send_message(self, data, request_id, action):
        await MessageModel.objects.acreate(
            room=self.room,
            user=self.scope['user'],
            text=data['text']
        )
        await self.channel_layer.group_send(
            self.room.name,
            {
                'type': 'sender',
                'message': data['text'],
                'user': self.user_name,
                'id': request_id
            }
        )
    @action()
    async def send_private_message(self, data, request_id, action):
        self.private_room_name = f'user_{data['userId']}'
        private_room, is_created = await ChatRoomModel.objects.aget_or_create(name=self.private_room_name, is_private=True)
        await private_room.users.aadd(await UserModel.objects.aget(pk=data['userId']), self.scope['user'])
        await MessageModel.objects.acreate(room=private_room, user=self.scope['user'], text=data['text'])
        await self.channel_layer.group_add(self.private_room_name, self.channel_name)
        await self.channel_layer.group_send(
            self.private_room_name,{
                'type': 'sender',
                'message': data['text'],
                'user': self.user_name,
                'id': request_id
            }
        )

    @database_sync_to_async
    def get_profile_name(self):
        user = self.scope['user']
        return user.profile.name

    @database_sync_to_async
    def get_last_five_messages(self):
        res = MessageModel.objects.filter(
            Q(room=self.room) | (Q(room__is_private=True) & Q(room__users__in=[self.scope['user']]))
        ).annotate(name=F('user__profile__name'), pk=F('user__pk')).values('text', 'name', 'pk').order_by('-id')[:5]
        return reversed([(f'{message['pk']}_{message['name']}', message['text']) for message in res])

