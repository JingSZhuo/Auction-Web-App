from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Item,User

from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    item_list= Item.objects.order_by('item_title')
    output = ', '.join((i.item_title for i in item_list))
    return HttpResponse(output)

@csrf_exempt