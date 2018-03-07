from django.shortcuts import render
from login.models import visitors
from datetime import date

# Create your views here.

def show_dashboard(request):
    last_ten = visitors.objects.all().order_by('-id')[:10][::-1]
    all_records = visitors.objects.all()
    visits_month = []
    month_names = []
    signups_month = []
    max_lineGraph = 0
    max_barGraph = 0
    total_visits = 0
    total_users = 0
    for i in range(0, len(all_records)):
        total_visits += all_records[i].visits
        total_users += all_records[i].signups
    for i in range(0, len(last_ten)):
        # print(last_ten[i].visits, last_ten[i].year, last_ten[i].month)
        visits_month.append(last_ten[i].visits)
        signups_month.append(last_ten[i].signups)
        if max_lineGraph < last_ten[i].visits:
            max_lineGraph = last_ten[i].visits
        if max_barGraph < last_ten[i].signups:
            max_barGraph = last_ten[i].signups
        value = date(2000, last_ten[i].month, 1).strftime('%b') + "'" + str(last_ten[i].year)[-2:]
        month_names.append(value)
    max_lineGraph = (int(max_lineGraph / 100)+2)*100
    max_barGraph = (int(max_barGraph / 100)+2)*100

    print(signups_month[-6:], month_names[-6:], max_lineGraph, max_barGraph)

    return render(request, 'dashboard/dashboard_home.html',
                  {
                      "visits_month": visits_month,
                       "signups_month": signups_month[-6:],
                       "signup_month_names": month_names[-6:],
                       "month_names": month_names,
                       "max_lineGraph": max_lineGraph,
                       "max_barGraph": max_barGraph,
                       "total_visits": total_visits,
                       "total_users": total_users
                   })
