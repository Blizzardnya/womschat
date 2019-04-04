from django.urls import path
from .views import RoomAPIView, DialogAPIView, AddUsersRoom


urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('dialog/', DialogAPIView.as_view()),
    path('users/', AddUsersRoom.as_view()),
]