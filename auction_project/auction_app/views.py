from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Item, CustomUserManager, CustomUser, Question, Answer
from django.views.generic.edit import CreateView

"""Form imports"""
from .forms import CustomUserSignupForm, CustomUserLoginForm

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
def usertest_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'users': [
                user.to_dict()
                for user in CustomUser.objects.all()
            ]
        })

    elif request.method == 'PUT':
        json_convert_to_dict = json.loads(request.body)

        identifier=json_convert_to_dict['user_id']
        print("userID")
        print(identifier)

        getID=CustomUser.objects.get(pk=identifier)

        getID=json_convert_to_dict['updated_pic']
        getID.save()

        return JsonResponse({
            'users' :[
                data.to_dict()
                for data in CustomUser.objects.all()
            
            ]        
        })
    else:
        pass

@csrf_exempt
def useremail_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'users': [
                user.to_dict()
                for user in CustomUser.objects.all()
            ]
        })
    if request.method == 'PUT':
        json_convert_to_dict = json.loads(request.body)

        identifier=json_convert_to_dict['user_id']
        print("userID")
        print(identifier)

        getID=CustomUser.objects.get(pk=identifier)

        print(getID)

        getID.email=json_convert_to_dict['user_email']
        print(getID)
        getID.save()

    return JsonResponse({
        'users' :[
            data.to_dict()
            for data in CustomUser.objects.all()
        
        ]        
    })

@csrf_exempt
def userdob_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'users': [
                user.to_dict()
                for user in CustomUser.objects.all()
            ]
        })
    if request.method == 'PUT':
        json_convert_to_dict = json.loads(request.body)

        identifier=json_convert_to_dict['user_id']
        print("userID")
        print(identifier)

        getID=CustomUser.objects.get(pk=identifier)
        print(getID)

        getID.date_of_birth=json_convert_to_dict['user_dob']
        getID.save()

    return JsonResponse({
        'users' :[
            data.to_dict()
            for data in CustomUser.objects.all()
        ]        
    })

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
def logout_page(request):
    logout(request)
    return redirect("http://127.0.0.1:8000")

@login_required
def hidden_page(request):
    return HttpResponse("Hidden page, You are still logged in")

@csrf_exempt
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:5173/')
    else:
        if request.method == 'POST':
            form = CustomUserSignupForm(request.POST)         #user input data passed into form
            if form.is_valid():
                print(request.POST['email'], request.POST['password1'])
                new_user = CustomUser.object.create_user(request.POST['email'], request.POST['password1'], "2000-01-01", "profile.png")
                new_user.save()
                print("created newuser: ", new_user)
                email = request.POST['email']
                password = request.POST['password1']
                user = authenticate(request, username=email, password=password)
                login(request, user)
                return redirect('http://127.0.0.1:5173/')
            else:
                print(request.POST['email'], request.POST['password1'], request.POST['password2'],"Invalid")
        #Any requests that is NOT POST (i.e. page refreshes) 
        form = CustomUserSignupForm()   
        return render(request, 'authentication/signup.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:5173/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:5173/')
        form = CustomUserLoginForm()
        return render(request, 'authentication/login.html', {'form': form})
    

@csrf_exempt
def profile_change(request):
    if request.method == 'POST':
        print("Uploaded..?" , request.body)
        return HttpResponse()


@csrf_exempt
def display_profile(request):
    if request.user.is_authenticated:
        print("username: " , request.user.username)
        return JsonResponse(
            {
                "id" : request.user.id,
                "username" : request.user.email,
                "date_of_birth": request.user.date_of_birth,
            }
        )
    else: return HttpResponse("Not logged in")

@csrf_exempt
def addQuestions_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'questions': [
                q.to_dict()
                for q in Question.objects.all()
            ]
        })
    if request.method == 'POST':
        json_convert_to_dict = json.loads(request.body)
        id=json_convert_to_dict['itemForeignKey']
        item=Item.objects.get(pk=id)
        question = Question.objects.create(
            question_text = json_convert_to_dict['questionText'],
            question_item = item
             
        ) 
        return JsonResponse(question.to_dict())

@csrf_exempt
def addAnswers_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'answers': [
                a.to_dict()
                for a in Answer.objects.all()
            ]
        })
    if request.method == 'POST':
        json_convert_to_dict = json.loads(request.body)
        id=json_convert_to_dict['questionForeignKey']
        question_obj=Question.objects.get(pk=id)
        answer = Answer.objects.create(
            question= question_obj,
            answers = json_convert_to_dict['answerText']   
        )
        return JsonResponse(answer.to_dict())
