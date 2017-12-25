from django.shortcuts import render

# Create your views here.
def show_news(request):
	return render(request, 'news/session_news.html', {})
