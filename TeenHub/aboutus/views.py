from django.shortcuts import render

# Create your views here.
def show_aboutus(request):
    return render(request, 'aboutus/about_us.html', {})