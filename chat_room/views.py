from django.db.models import Q
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import Room, Chat
from .serializers import RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializer
# Create your views here.


class RoomAPIView(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user)|Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creator=request.user)
        return Response(status=201)


class DialogAPIView(APIView):
    """Диалог чата"""
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = get_object_or_404(Room, pk=request.GET.get("id"))
        invited = room.invited.values_list('pk', flat=True)
        users = User.objects.exclude(pk__in=list(invited))
        # users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)
