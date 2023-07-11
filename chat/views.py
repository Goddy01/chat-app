from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .models import Room
# Create your views here.

@require_POST
def create_room(request):
    name = request.POST.get('name', '')
    url = request.POST.get('url', '')

    Room.objects.create(
        client=name,
        url=url
    )
    return JsonResponse({'message': 'room created'})