from django.shortcuts import render, redirect

# Create your views here.
def logout(request):
    del request.session["id"]
    return render(request, 'home/home.html', {})

def show_movies(request):
    return render(request, 'movies/session.html', {})

def show_movie_info(request, movieid):
    request.session["movieid"] = movieid
    return render(request, 'movies/viewInfoMovies.html', {})
