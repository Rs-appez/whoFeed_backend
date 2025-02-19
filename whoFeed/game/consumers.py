from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer


class TicksSyncConsumer(SyncConsumer):
    def __get_party(self):
        return self.scope["url_route"]["kwargs"]["party_ID"]

    def websocket_connect(self, event):
        self.send({"type": "websocket.accept"})

        group_name = self.__get_party()
        # Join ticks group
        async_to_sync(self.channel_layer.group_add)(
            group_name, self.channel_name)

    def websocket_disconnect(self, event):
        group_name = self.__get_party()
        # Leave ticks group
        async_to_sync(self.channel_layer.group_discard)(
            group_name, self.channel_name)

    def new_ticks(self, event):
        self.send(
            {
                "type": "websocket.send",
                "text": event["content"],
            }
        )
