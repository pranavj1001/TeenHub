from django.shortcuts import render
from login.models import visitors
from datetime import date

# Create your views here.

def show_dashboard(request):
    last_ten = visitors.objects.all().order_by('-id')[:10][::-1]
    visits_month = []
    month_names = []
    max = 0
    for i in range(0, len(last_ten)):
        # print(last_ten[i].visits, last_ten[i].year, last_ten[i].month)
        visits_month.append(last_ten[i].visits)
        if max < last_ten[i].visits:
            max = last_ten[i].visits
        value = date(2000, last_ten[i].month, 1).strftime('%b') + "'" + str(last_ten[i].year)[-2:]
        month_names.append(value)
    max += 100

    return render(request, 'dashboard/dashboard_home.html', {"visits_month": visits_month, "month_names": month_names, "max": max})
