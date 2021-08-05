# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def chat(request):
    return render(request, 'draw/chat.html')

def pie(request):
    return render(request, 'draw/pie.html')

def button(request):
    return render(request, 'draw/button.html')

def activities(request):
    return render(request, 'draw/activities.html')


def days(request):
    return render(request, 'draw/days.html')

def lovetracker(request):
    return render(request, 'draw/lovetracker.html')

def share(request):
    return render(request, 'draw/share.html')


def summary(request):
    return render(request, 'draw/summary.html')

def topics(request):
    return render(request, 'draw/topics.html')
