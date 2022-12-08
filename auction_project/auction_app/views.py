from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Item, CustomUserManager, CustomUser
from django.views.generic.edit import CreateView

from .forms import CusomUserCreationForm

import json

from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    item_list= Item.objects.order_by('item_title')
    output = ', '.join((i.item_title for i in item_list))
    return HttpResponse(output, "Auction in development...")

@csrf_exempt
def addItems_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })
    if request.method == 'POST':
        json_convert_to_dict = json.loads(request.body)
        item = Item.objects.create(
            item_title = json_convert_to_dict['itemTitle'],
            item_description = json_convert_to_dict['itemDescription'],
            item_sprice = json_convert_to_dict['itemStartingPrice'],
            item_picture = json_convert_to_dict['itemPicture'],
            item_auctionfinish = json_convert_to_dict['itemActionFinish'],
        ) 
        return JsonResponse(item.to_dict())
    else:
        pass

@csrf_exempt
def signup_page(request):
    if request.method == 'POST':
        user = CustomUser.object.create_user("email@email.com", "password123", "2022-12-08", "png.png")
        user.save()
    return HttpResponse("Created!")

        


def login_page(request):
    return render(request, 'authentication/login.html')



# def car_api(request: HttpRequest, car_id: int) -> HttpResponse:
#     car = get_object_or_404(Car, id=car_id)

#     if request.method == 'GET':
#         return JsonResponse(car.to_dict())