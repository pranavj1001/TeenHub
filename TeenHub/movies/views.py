from django.shortcuts import render

# Create your views here.
def show_movies(request):
    return render(request, 'movies/movies.html', {})
