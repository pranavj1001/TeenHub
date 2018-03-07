from django.shortcuts import render
from login.models import visitors, User
from datetime import date
from .models import feed

# Create your views here.

def show_dashboard(request):
    # Graph Logic
    last_ten_graph = visitors.objects.all().order_by('-id')[:10][::-1]
    all_records_graph = visitors.objects.all()
    visits_month = []
    month_names = []
    signups_month = []
    max_lineGraph = 0
    max_barGraph = 0
    total_visits = 0
    total_users = 0

    for i in range(0, len(all_records_graph)):
        total_visits += all_records_graph[i].visits
        total_users += all_records_graph[i].signups
    for i in range(0, len(last_ten_graph)):
        visits_month.append(last_ten_graph[i].visits)
        signups_month.append(last_ten_graph[i].signups)
        if max_lineGraph < last_ten_graph[i].visits:
            max_lineGraph = last_ten_graph[i].visits
        if max_barGraph < last_ten_graph[i].signups:
            max_barGraph = last_ten_graph[i].signups
        value = date(2000, last_ten_graph[i].month, 1).strftime('%b') + "'" + str(last_ten_graph[i].year)[-2:]
        month_names.append(value)
    max_lineGraph = (int(max_lineGraph / 100)+2)*100
    max_barGraph = (int(max_barGraph / 100)+2)*100

    # News Feed Logic
    feed_content = []
    feed_createdBy = []
    feed_time = []
    feed_comments = []
    last_four_feed = feed.objects.all().order_by('-id')[:4]

    for i in range(0, len(last_four_feed)):
        if User.objects.filter(id=last_four_feed[i].createdBy).exists():
            user = User.objects.get(id=last_four_feed[i].createdBy)
            feed_createdBy.append(user.name)
        else:
            feed_createdBy.append("Anonymous")
        feed_comments.append(last_four_feed[i].comments)
        feed_time.append(last_four_feed[i].createdAt)
        feed_content.append(last_four_feed[i].message)

    return render(request, 'dashboard/dashboard_home.html',
                  {
                    "visits_month": visits_month,
                    "signups_month": signups_month[-6:],
                    "signup_month_names": month_names[-6:],
                    "month_names": month_names,
                    "max_lineGraph": max_lineGraph,
                    "max_barGraph": max_barGraph,
                    "total_visits": total_visits,
                    "total_users": total_users,
                    "feed_content": feed_content,
                    "feed_createdBy": feed_createdBy,
                    "feed_time": feed_time,
                    "feed_comments": feed_comments
                  })
