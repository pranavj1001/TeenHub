from django.shortcuts import render, redirect

# Create your views here.
def logout(request):
    print("deleted session")
    del request.session["id"]
    return render(request, 'home/home.html', {})

def show_movies(request):
    return render(request, 'movies/session.html', {})

