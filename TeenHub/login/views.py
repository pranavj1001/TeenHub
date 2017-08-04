from django.shortcuts import render

# Create your views here.
def show_login(request):
    return render(request, 'login/login.html', {})

def show_signup(request):
    return render(request, 'login/signup.html', {})