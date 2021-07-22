# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def chat(request):
    return render(request, 'draw/chat.html')


def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
