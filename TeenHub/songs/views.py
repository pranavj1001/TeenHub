from django.shortcuts import render

# Create your views here.
def show_songs(request):
    return render(request, 'songs/songs.html', {})
