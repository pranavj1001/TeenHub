from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from .models import User
import datetime
from datetime import date

# Create your views here.
def show_login(request):
    return render(request, 'login/login.html', {})

def show_signup(request):
    return render(request, 'login/signup.html', {})

def signup_user(request):
    if request.method == 'GET':
        return render(request, "register.html", {})
    if request.POST:
        print('signup, everything is fine')
        name = request.POST['name']
        username = request.POST['username']
        dateofbirth = datetime.datetime.strptime(request.POST['DOB'], "%d-%m-%Y").date()
        email = request.POST['email']
        password = request.POST['password']
        today = date.today()
        age = today.year - dateofbirth.year - ((today.month, today.day) < (dateofbirth.month, dateofbirth.day))
        if (len(name) == 0 or len(email) == 0):
            print("User already exists")
            # return render_to_response('alertmessage.html', {"message": 'all feilds are neccesory'})
        if User.objects.filter(username=username).exists():
            return HttpResponse("user already exists")
        else:
            existing_number_of_users = User.objects.count()
            existing_number_of_users += 1
            newUser = User(user_number=existing_number_of_users, name=name, username=username, dob=dateofbirth, age=age, email=email, password=password)
            newUser.save()
            return HttpResponse("you're in")

def login_user(request):
    return render("logged in")