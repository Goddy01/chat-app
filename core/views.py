from django.shortcuts import render
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')