from django.urls import path
from .views import RoomAPIView, DialogAPIView


urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('dialog/', DialogAPIView.as_view()),
]