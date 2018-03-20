from django.shortcuts import render

# Create your views here.
def show_songs(request):
    return render(request, 'songs/session.html',{})

def show_song_info(request,songsinfo,type):
    if type == "1":
        print("artist")
        return render(request, 'songs/viewInfoArtistSongs.html', {'songsinfo':songsinfo,'type':type})
    elif type == "2":
        print("tracks")
        return render(request, 'songs/viewInfoTrackSongs.html', {'songsinfo':songsinfo,'type':type})
    else:
        print("albums")
        return render(request, 'songs/viewInfoAlbumSongs.html', {'songsinfo':songsinfo,'type':type})
