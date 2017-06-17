import pandas as pd
import numpy as np
from scipy import spatial
import operator

# data frame
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('PATH', sep='\t', names=r_cols, usecols=range(3))

# combine all the movies with their ratings
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
# lambda function to calculate the popularity of a movie in a range of 0 (least popular) - 1 (most popular)
# Logic: divide the (difference of popularity of current movie with the least popular movie) with the (range i.e. (differnce of most popular and least popular movie))
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

movieDict = {}
with open(r'PATH') as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        # get one line at a time and split it w.r.t. every different field
        fields = line.rstrip('\n').split('|')
        # first field is about movie_id
        movieID = int(fields[0])
        # second field is about name of the movie
        name = fields[1]
        # there are 19 different genres, stored with 0 or 1
        genres = fields[5:25]
        genres = map(int, genres)
        # create movieDict Dictionary
        # contains: name, genres, popularity, average rating
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

# combine all the info gathered above and form a distance metrics
# takes two movie ids and computes the distance score between the two
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    # construct a cosine similarity metric between the two movies
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    # compare the popularity scores
    popularityDistance = abs(popularityA - popularityB)
    # return the sum
    return genreDistance + popularityDistance

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        # dont compute if movie and movieID are same
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    # sort the above result
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    # make a list of K neighbors
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

# 10 neighbors
K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
# iterate through 10 neighbors and compute avg rating from each neighbor
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))
    
avgRating /= K

avgRating

movieDict[1]