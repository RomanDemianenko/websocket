import asyncio
import json

from channels.generic.websocket import AsyncWebsocketConsumer

from webtest.models import TrafficLight


class TrafficLights(AsyncWebsocketConsumer):

    async def websocket_connect(self, message):
        self.room_name = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f'Traffic_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'exam_texting',
                'pk': self.room_name,
            }
        )
        await self.accept()

    async def text(self):
        light_time = TrafficLight.objects.get(pk=self.room_name).duration.second
        for second in range(light_time, -1, -1):
            await self.send(
                json.dumps(
                    {'message': (TrafficLight.objects.get(pk=self.room_name).text, " lights left", str(second))}))
            await asyncio.sleep(1)

    async def exam_texting(self):
        await self.send(text_data=json.dumps({
            'text': await self.text()
        }))

    async def websocket_receive(self, message):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'exam_texting',
                'pk': self.room_name,
            }
        )

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
