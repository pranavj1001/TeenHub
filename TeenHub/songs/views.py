from django.shortcuts import render

# Create your views here.
def show_songs(request):
    if 'id' in request.session:
        return render(request, 'songs/session.html',{})
    return render(request, 'songs/songs.html', {})
