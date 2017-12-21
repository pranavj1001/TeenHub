from django.shortcuts import render, redirect
import pandas as pd
from .models import Links, Ratings
import simplejson as json
from TeenHub.settings import PROJECT_ROOT

# Create your views here.
def logout(request):
    del request.session["id"]
    for i in range(1, 11):
        string = 'recommendationsMovies'
        string += str(i)
        if (string) in request.session:
            del request.session[string]
    if 'movie_rating' in request.session:
        del request.session['movie_rating']
    return render(request, 'home/home.html', {})

def show_movies(request):

    if 'movie_rating' in request.session:
        del request.session['movie_rating']

    if 'id' in request.session:
        userRatings = pd.read_csv(PROJECT_ROOT + '/movies/datasets/userRatings.csv')
        corrMatrix = userRatings.corr(method='pearson', min_periods=20)

        # if 'movieRecommender' not in request.session:
        #     print("computing")
        #     corrMatrix = userRatings.corr(method='pearson', min_periods=20)
        #     request.session.movieRecommender = corrMatrix
        #     print("computing")
        # else:
        #     print("not computing")
        #     corrMatrix = request.session["movieRecommender"]

        getRatings = userRatings.loc[0].dropna()

        similarCandidates = pd.Series()
        for i in range(0, len(getRatings)):
            recommendationList = corrMatrix[getRatings.index[i]].dropna()
            if getRatings[i] > 4.0:
                recommendationList = recommendationList.map(lambda x: 2 * x * getRatings[i])
            elif getRatings[i] <= 4.0 and getRatings[i] > 3.0:
                recommendationList = recommendationList.map(lambda x: x * getRatings[i])
            elif getRatings[i] <= 3.0 and getRatings[i] > 2.5:
                recommendationList = recommendationList.map(lambda x: x + getRatings[i])
            elif getRatings[i] <= 2.5:
                recommendationList = recommendationList.map(lambda x: (-1) * x - getRatings[i])
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

    return render(request, 'movies/session.html', {})

def show_movie_info(request, movieid):
    request.session["movieid"] = movieid
    if 'movie_rating' in request.session:
        del request.session['movie_rating']
    print("here")
    if 'id' in request.session:
        if Ratings.objects.filter(user_id=request.session["id"], movie_id=request.session["movieid"]).exists():
            ratingRow = Ratings.objects.get(user_id=request.session["id"], movie_id=request.session["movieid"])
            request.session["movie_rating"] = json.dumps(ratingRow.ratings)
    return render(request, 'movies/viewInfoMovies.html', {})

def save_movie_rating(request, movie_rating):
    if 'id' in request.session:
        if Ratings.objects.filter(user_id=request.session["id"], movie_id=request.session["movieid"], ratings=movie_rating).exists():
          print('rating already exists')
          return render(request, 'movies/viewInfoMovies.html', {})
        elif Ratings.objects.filter(user_id=request.session["id"], movie_id=request.session["movieid"]).exists():
            print('user wants to enter a new rating for a movie which he/she already rated')
            Ratings.objects.filter(user_id=request.session["id"], movie_id=request.session["movieid"]).delete()
        newRating = Ratings(user_id=request.session["id"], movie_id=request.session["movieid"], ratings=movie_rating)
        newRating.save()
        show_movie_info(request, request.session["movieid"])
    return render(request, 'movies/viewInfoMovies.html', {})
