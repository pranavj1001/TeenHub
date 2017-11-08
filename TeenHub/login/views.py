from django.http import HttpResponse
from django.shortcuts import render,redirect
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
        # return render_to_response('alertmessage.html', {"message": 'all feilds are neccesory'})
        return HttpResponse("Don't use GET method")
    if request.POST:
        print('signup, everything is fine')
        name = request.POST['name']
        username = request.POST['username']
        dateofbirth = datetime.datetime.strptime(request.POST['DOB'], "%d-%m-%Y").date()
        email = request.POST['email']
        password = request.POST['password']
        today = date.today()
        age = today.year - dateofbirth.year - ((today.month, today.day) < (dateofbirth.month, dateofbirth.day))
        if (len(name) == 0 or len(email) == 0 or len(password) == 0):
            print("name, email password not entered yet")
            # return render_to_response('alertmessage.html', {"message": 'all feilds are neccesory'})
        if User.objects.filter(username=username).exists():
            return HttpResponse("user already exists")
        else:
            existing_number_of_users = User.objects.count()
            existing_number_of_users += 1
            newUser = User(user_number=existing_number_of_users, name=name, username=username, dob=dateofbirth, age=age, email=email, password=password)
            newUser.save()
            userDetails = User.objects.get(username=username)
            request.session["id"] = userDetails.id
            return redirect('/movies')

def login_user(request):
    if request.method == 'GET':
        # return render_to_response('alertmessage.html', {"message": 'all feilds are neccesory'})
        return HttpResponse("Don't use GET method")
    if request.POST:
        print('login, everything is fine')
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            userDetails = User.objects.get(username=username)
            if password == str(userDetails.password):
                request.session["id"] = userDetails.id
                return redirect('/movies')
            else:
                return HttpResponse("Wrong Password")
        else:
            return HttpResponse("Could not find this user")