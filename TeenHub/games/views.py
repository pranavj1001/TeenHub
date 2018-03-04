from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def games_home (request):
	return render(request,'games/session_games.html')

def show_game_info(request, gameid):
	return render(request, 'games/viewInfoGames.html', {})
