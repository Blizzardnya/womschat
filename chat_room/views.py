from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import permissions

from .models import Room, Chat
from .serializers import RoomSerializers
# Create your views here.


class RoomAPIView(APIView):
    """Комнаты чата"""

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})
