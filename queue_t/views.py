# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'queue_t/summary.html')

def chat(request):
    return render(request, 'queue_t/chat.html')

def activities(request):
    return render(request, 'queue_t/activities.html')

def days(request):
    return render(request, 'queue_t/days.html')

def lovetracker(request):
    return render(request, 'queue_t/lovetracker.html')

def share(request):
    return render(request, 'queue_t/share.html')

def summary(request):
    return render(request, 'queue_t/summary.html')

def topics(request):
    return render(request, 'queue_t/topics.html')

def onetopic(request):
    return render(request, 'queue_t/onetopic.html')

def daysinput(request):
    return render(request, 'queue_t/daysinput.html')

def settings(request):
    return render(request, 'queue_t/settings.html')

def about_us(request):
    return render(request, 'queue_t/about_us.html')

def profile(request):
    return render(request, 'queue_t/profile.html')

def randomTopics_one(request):
    return render(request, 'queue_t/randomTopics_one.html')

def randomTopics_two(request):
    return render(request, 'queue_t/randomTopics_two.html')

def randomTopics(request):
    return render(request, 'queue_t/randomTopics.html')

def activitiesinput(request):
    return render(request, 'queue_t/activitiesinput.html')

def trackerinput(request):
    return render(request, 'queue_t/trackerinput.html')

