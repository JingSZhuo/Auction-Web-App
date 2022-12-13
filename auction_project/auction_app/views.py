from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Item, CustomUserManager, CustomUser
from django.views.generic.edit import CreateView

"""Form imports"""
from .forms import CustomUserSignupForm

"""Authentication packages"""
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

"""JSON import"""
import json


"""CSRF EXEMPTION"""
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

    elif request.method == 'PUT':
        json_convert_to_dict = json.loads(request.body)

        identifier=json_convert_to_dict['item_id']
        print("itemID")
        print(identifier)

        getID=Item.objects.get(pk=identifier)

        getID.item_personHighestBid=json_convert_to_dict['updated_email']
        print(getID.item_personHighestBid)
        getID.item_sprice=json_convert_to_dict['updated_sprice']
        getID.save()

        return JsonResponse({
            'items' :[
                data.to_dict()
                for data in Item.objects.all()
            
            ]        
        })


    else:
        pass

@csrf_exempt
def signup_page(request):
    if request.method == 'POST':
        json_convert_to_python_dictionary = json.loads(request.body)
        user = CustomUser.object.create_user(
                json_convert_to_python_dictionary['email'], 
                json_convert_to_python_dictionary['password'],
                json_convert_to_python_dictionary['dob'], 
                json_convert_to_python_dictionary['image'],
            )
        user.save()
    return HttpResponse("Created!")


@csrf_exempt
def redirect_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponse("Logged in")
        else:
            return HttpResponse("Not logged in")
    else:
        return HttpResponse("Null")

@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        email_json = json.loads(request.body)['email']
        password_json = json.loads(request.body)['password']
        user = authenticate(request, username=email_json, password=password_json)
        if user is not None:
            login(request, user)
            return HttpResponse("Successfully Logged in")
        else:
            return HttpResponse("Failed to login with: " + email_json + " " + password_json)
    if request.method == 'GET': 
            if request.user.is_authenticated:
                return HttpResponse("Logged in")
            else:
                return HttpResponse("Not logged in")
    #json_convert_to_python_dictionary = json.loads(request.body)
    # #print(json_convert_to_python_dictionary)
    # email = json_convert_to_python_dictionary['email']
    # password = json_convert_to_python_dictionary['password']
    # email_string = json.dumps(email)
    # password_string = json.dumps(password)
    # print(email_string + " " + password_string)
    # email = "test@gmail.com"
    # password = "password"
    # user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
    # if user is not None:
    #     login(request, user)
    #     return HttpResponse("Successfully Logged in")
    # else:
    #     return HttpResponse("Failed to login with: "+ email+ " "+ password)
    
@csrf_exempt        
def logout_page(request):
    logout(request)
    return HttpResponse("Logged out")

@login_required
def hidden_page(request):
    return HttpResponse("Hidden page, You are still logged in")

@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:5173/')
    else:
        if request.method == 'POST':
            form = CustomUserSignupForm(request.POST)         #user input data passed into form
            if form.is_valid():
                print(request.POST['email'], request.POST['password1'])
                new_user = CustomUser.object.create_user(request.POST['email'], request.POST['password1'], "2022-02-02", "png.png")
                new_user.save()
                return redirect('http://127.0.0.1:5173/')
            else:
                print(request.POST['email'], request.POST['password1'], request.POST['password2'],"Invalid")
        #Any requests that is NOT POST (i.e. page refreshes) 
        form = CustomUserSignupForm()   
        return render(request, 'authentication/signup.html', {'form': form})



# def car_api(request: HttpRequest, car_id: int) -> HttpResponse:
#     car = get_object_or_404(Car, id=car_id)

#     if request.method == 'GET':
#         return JsonResponse(car.to_dict())