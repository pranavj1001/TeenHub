from django.shortcuts import render, redirect
import pandas as pd
from .models import Links, Ratings
import simplejson as json
from TeenHub.settings import PROJECT_ROOT
from datetime import date
from django.http import HttpRequest
import ipaddress

# Create your views here.
def logout(request):
    if 'id' in request.session:
        del request.session["id"]
    for i in range(1, 11):
        string = 'recommendationsMovies'
        string += str(i)
        if (string) in request.session:
            del request.session[string]
    if 'movie_rating' in request.session:
        del request.session['movie_rating']
    if 'show_rating_stars' in request.session:
        del request.session["show_rating_stars"]
    if 'noRatings' in request.session:
        del request.session["noRatings"]
    if 'genre_id' in request.session:
        del request.session['genre_id']
    if 'ratingsChanged' in request.session:
        del request.session['ratingsChanged']

    return render(request, 'home/home.html', {})

def show_movies(request):

    if 'movie_rating' in request.session:
        del request.session['movie_rating']

    if 'show_rating_stars' in request.session:
        del request.session["show_rating_stars"]

    request.session["noRatings"] = 1

    if 'id' in request.session:
        request.session["noRatings"] = 0
        if not 'recommendationsMovies1' in request.session or 'ratingsChanged' in request.session:
            print('ratingsChanged')

            if 'ratingsChanged' in request.session:
                del request.session['ratingsChanged']

            dataset_ratings = pd.read_csv(PROJECT_ROOT + '/movies/datasets/movies_ratings_small.csv', usecols=range(3))

            currentUserRatings = Ratings.objects.filter(user_id=request.session['id'])

            if(len(currentUserRatings) > 0):
                for i in range(0, len(currentUserRatings)):
                    dataset_ratings = dataset_ratings.append({'userId': 672, 'movieId': currentUserRatings[i].movie_id, 'rating': int(currentUserRatings[i].ratings)}, ignore_index=True)
                # print(dataset_ratings)

                userRatings = dataset_ratings.pivot_table(index=['userId'], columns=['movieId'], values='rating')
                corrMatrix = userRatings.corr(method='pearson', min_periods=3)

                # if 'movieRecommender' not in request.session:
                #     print("computing")
                #     corrMatrix = userRatings.corr(method='pearson', min_periods=20)
                #     request.session["movieRecommender"] = json.dumps(corrMatrix)
                # else:
                #     print("not computing")
                #     corrMatrix = request.session["movieRecommender"]

                getRatings = userRatings.loc[672].dropna()

                similarCandidates = pd.Series()
                for i in range(0, len(getRatings)):
                    recommendationList = corrMatrix[getRatings.index[i]].dropna()
                    if getRatings.index[i] > 4.0:
                        recommendationList = recommendationList.map(lambda x: 2 * x * getRatings.index[i])
                    elif getRatings.index[i] <= 4.0 and getRatings.index[i] > 3.0:
                        recommendationList = recommendationList.map(lambda x: x * getRatings.index[i])
                    elif getRatings.index[i] <= 3.0 and getRatings.index[i] > 2.5:
                        recommendationList = recommendationList.map(lambda x: x + getRatings.index[i])
                    elif getRatings.index[i] <= 2.5:
                        recommendationList = recommendationList.map(lambda x: (-1) * x - getRatings.index[i])
                    similarCandidates = similarCandidates.append(recommendationList)

                similarCandidates.sort_values(inplace=True, ascending=False)  # sort the results

                # use groupby() to add together the scores from movies that show up more than once
                similarCandidates = similarCandidates.groupby(similarCandidates.index).sum()

                similarCandidates.sort_values(inplace=True, ascending=False)

                # filter out movies that the user already rated
                filteredRecommendationList = similarCandidates.drop(getRatings.index)
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[0])
                request.session["recommendationsMovies1"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[1])
                request.session["recommendationsMovies2"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[2])
                request.session["recommendationsMovies3"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[3])
                request.session["recommendationsMovies4"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[4])
                request.session["recommendationsMovies5"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[5])
                request.session["recommendationsMovies6"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[6])
                request.session["recommendationsMovies7"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[7])
                request.session["recommendationsMovies8"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[8])
                request.session["recommendationsMovies9"] = link.tmdb_id
                link = Links.objects.get(movie_id=filteredRecommendationList.head(10).index[9])
                request.session["recommendationsMovies10"] = link.tmdb_id

            else:
                request.session["noRatings"] = 1



    return render(request, 'movies/session.html', {})

def show_movie_info(request, movieid):
    request.session["movieid"] = movieid

    if 'movie_rating' in request.session:
        del request.session['movie_rating']

    if 'id' in request.session:
        if Links.objects.filter(tmdb_id=movieid).exists():
            request.session["show_rating_stars"] = True
            link = Links.objects.get(tmdb_id=movieid)
            if Ratings.objects.filter(user_id=request.session["id"], movie_id=link.movie_id).exists():
                ratingRow = Ratings.objects.get(user_id=request.session["id"], movie_id=link.movie_id)
                request.session["movie_rating"] = json.dumps(ratingRow.ratings)
                print(request.session["movie_rating"])

        elif 'show_rating_stars' in request.session:
            del request.session["show_rating_stars"]

    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    #print("outside")
    #print(ip)
    if ip:
        # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
        ip = ip.split(", ")[0]
        #print("if")
        #print(ip)
    else:
        ip = request.META.get("REMOTE_ADDR", "")
        #print("else")
        #print(ip)


    return render(request, 'movies/viewInfoMovies.html', {"ip":ip})

def show_genre_list(request, genre_id):
    print(genre_id)
    request.session['genre_id'] = genre_id
    return render(request, 'movies/genres_list.html', {})

def save_movie_rating(request, movie_rating):
    print(movie_rating)
    today = date.today()
    if 'noRatings' in request.session:
        del request.session["noRatings"]
    if 'id' in request.session:
        link = Links.objects.get(tmdb_id=request.session["movieid"])
        if Ratings.objects.filter(user_id=request.session["id"], movie_id=link.movie_id, ratings=movie_rating).exists():
          print('rating already exists')
          return render(request, 'movies/viewInfoMovies.html', {})
        elif Ratings.objects.filter(user_id=request.session["id"], movie_id=link.movie_id).exists():
            print('user wants to enter a new rating for a movie which he/she already rated')
            oldRating = Ratings.objects.get(user_id=request.session["id"], movie_id=link.movie_id)
            oldRating.ratings = movie_rating
            oldRating.day = today.day
            oldRating.month = today.month
            oldRating.year = today.year
            oldRating.edited = 1
            oldRating.save()
            request.session['ratingsChanged'] = 1
        else:
            newRating = Ratings(user_id=request.session["id"], movie_id=link.movie_id, ratings=movie_rating, day=today.day, month=today.month, year=today.year, edited=0)
            newRating.save()
            request.session['ratingsChanged'] = 1
        show_movie_info(request, request.session["movieid"])
    return render(request, 'movies/viewInfoMovies.html', {})
