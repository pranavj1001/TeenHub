from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from login.models import visitors, User
from movies.models import Ratings, Links
from datetime import date
from .models import feed

# Create your views here.

def fill_ratings_per_month(request, year, ratings_values):
    ratings_per_month = []
    max = 0

    if Ratings.objects.filter(year=year).exists():
        for i in range(1, 13):
            if Ratings.objects.filter(year=year, month=i, user_id=request.session['id']).exists():
                temp = Ratings.objects.filter(year=year, month=i, user_id=request.session['id']).count()
                ratings_per_month.append(temp)
                if max < temp:
                    max = temp

                ratings = Ratings.objects.filter(year=year, month=i, user_id=request.session['id'])
                for j in range(0, len(ratings)):
                    ratings_values[int(ratings[j].ratings) - 1] += 1

            else:
                ratings_per_month.append(0)

    return {
                "ratings_per_month": ratings_per_month,
                "max": max,
                "ratings_values": ratings_values
           }

def return_news_details(choice):
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
    max_lineGraph = (int(max_lineGraph / 100) + 2) * 100
    max_barGraph = (int(max_barGraph / 100) + 2) * 100

    # News Feed Logic
    feed_content = []
    feed_createdBy = []
    feed_time = []
    feed_comments = []

    if choice == 0:
        last_four_feed = feed.objects.all().order_by('-id')[:4]
    else:
        last_four_feed = feed.objects.all().order_by('-id')

    for i in range(0, len(last_four_feed)):
        if User.objects.filter(id=last_four_feed[i].createdBy).exists():
            user = User.objects.get(id=last_four_feed[i].createdBy)
            feed_createdBy.append(user.name)
        else:
            feed_createdBy.append("Anonymous")
        feed_comments.append(last_four_feed[i].comments)
        feed_time.append(last_four_feed[i].createdAt)
        feed_content.append(last_four_feed[i].message)

    return {
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
           }

# common code
def return_movies_activities_details(request, year):
    ratings_per_month = []
    max = 0
    message = ''
    ratings_values = [0, 0, 0, 0, 0]
    total_ratings = 0
    rating_date = []
    rating_movie_id = []
    rating_number = []
    rating_edited = []

    # if user is logged in
    if 'id' in request.session:
        # if there are ratings of user present in the dataset
        if Ratings.objects.filter(user_id=request.session['id']).exists():
            print('there are ratings from this user')
            total_ratings = Ratings.objects.filter(user_id=request.session['id']).count()

            rating = Ratings.objects.filter(user_id=request.session['id'])
            for i in range(0, len(rating)):
                newDate = date(rating[i].year, rating[i].month, rating[i].day).strftime("%d, %B %Y")
                rating_date.append(newDate)
                link = Links.objects.get(movie_id=rating[i].movie_id)
                rating_movie_id.append(link.tmdb_id)
                rating_number.append(float(rating[i].ratings))
                rating_edited.append(rating[i].edited)

            # if there are ratings of user from the current year
            if Ratings.objects.filter(year=year, user_id=request.session['id']).exists():
                print('user has rated movies in this year')
                temp = fill_ratings_per_month(request, year, ratings_values)
                ratings_per_month = temp["ratings_per_month"]
                max = temp["max"]
                ratings_values = temp["ratings_values"]
            # if there are ratings of user from the current year
            else:
                print('user has not rating any movies in current year')
                message = 'You have not rated any movies in the year ' + str(year)

        # if there are no ratings of user present in the dataset
        else:
            print('there are no ratings')
            message = 'You have not rated any movies'

        max += (10 - (max % 10))

        return {
                  "ratings_per_month": ratings_per_month,
                  "year": year,
                  "max": max,
                  "message": message,
                  "ratings_values": ratings_values,
                  "total_ratings": total_ratings,
                  "rating_date": rating_date,
                  "rating_movie_id": rating_movie_id,
                  "rating_number": rating_number,
                  "rating_edited": rating_edited
              }
    # if user is not logged in
    else:
        return {}

def show_dashboard(request):
    dictionary = return_news_details(0)
    return render(request, 'dashboard/dashboard_home.html', dictionary)

def show_dashboard_with_full_news(request):
    dictionary = return_news_details(1)
    return render(request, 'dashboard/dashboard_home.html', dictionary)

def show_dashboard_movies(request):
    today = date.today()
    dictionary = return_movies_activities_details(request, today.year)
    return render(request, 'dashboard/dashboard_activities_movies.html', dictionary)

def show_dashboard_movies_custom_year(request, year):
    dictionary = return_movies_activities_details(request, year)
    return render(request, 'dashboard/dashboard_activities_movies.html', dictionary)

def show_dashboard_change_password(request):
    return render(request, 'dashboard/dashboard_change_password.html', {})

def change_password(request):
    print(request.POST['currentPassword'])
    print(request.POST['newPassword'])
    print(request.POST['newConfirmPassword'])

    message = ''
    if 'id' in request.session:
        currentUser = User.objects.get(id=request.session['id'])

        if not check_password(request.POST['currentPassword'], str(currentUser.password)):
            message = 'Your current password did not match with the password stored at our database.'
            print(message)
        elif request.POST['newPassword'] != request.POST['newConfirmPassword']:
            message = 'Your new password did not match. Please Enter same password in last two fields.'
            print(message)
        else:
            currentUser.password = make_password(request.POST['newPassword'])
            currentUser.save()
            message = 'Your password was successfully changed.'
            print(message)


    return render(request, 'dashboard/dashboard_change_password.html', {})