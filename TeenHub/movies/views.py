from django.shortcuts import render, redirect
import pandas as pd
from .models import Links

# Create your views here.
def logout(request):
    del request.session["id"]
    for i in range(1, 11):
        string = 'recommendationsMovies'
        string += str(i)
        if (string) in request.session:
            del request.session[string]
    return render(request, 'home/home.html', {})

def show_movies(request):

    if 'id' in request.session:
        userRatings = pd.read_csv('D:/PRANAV/Machine Learning/MovieRecommender/TeenHub/movies/datasets/userRatings.csv')

        if 'movieRecommender' not in request.session:
            print("computing")
            corrMatrix = userRatings.corr(method='pearson', min_periods=20)
            request.session.movieRecommender = corrMatrix
            request.session.save()
            print("computing")
        else:
            print("not computing")
            corrMatrix = request.session["movieRecommender"]

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
        print(similarCandidates)

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
    return render(request, 'movies/viewInfoMovies.html', {})
