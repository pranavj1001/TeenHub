from django.shortcuts import render

# Create your views here.
def show_songs(request):
    return render(request, 'songs/session.html',{})

def show_song_info(request,songsinfo,name,type):

    if type == "1":
        print("artist")
        return render(request, 'songs/viewInfoArtistSongs.html', {'songsinfo':songsinfo,'name':name,'type':type})
    elif type == "2":
        print("tracks")
        return render(request, 'songs/viewInfoTrackSongs.html', {'songsinfo':songsinfo,'name':name,'type':type})
    elif type == "3":
        print("albums")
        return render(request, 'songs/viewInfoAlbumSongs.html', {'songsinfo':songsinfo,'name':name,'type':type})
