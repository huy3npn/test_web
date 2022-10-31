from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from chats.serializers import MessageModelSerializer, MessageSerializer


class MessageView(CreateAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(pk=1)
        # print("[+-+]"+str(user))
        return self.create(request, *args, **kwargs)
