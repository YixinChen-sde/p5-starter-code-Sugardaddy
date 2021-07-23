# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def chat(request):
    return render(request, 'draw/chat.html')

def button(request):
    return render(request, 'draw/button.html')
