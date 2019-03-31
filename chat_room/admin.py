from django.contrib import admin
from .models import Room, Chat

# Register your models here.


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "text", "date")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("creator", "display_invited", "date")


