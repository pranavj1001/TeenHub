import pandas as pd

# dataframe for ratings
r_cols = ['user_id', 'movie_id', 'rating'] # our new dataFrame will have 3 columns
# be careful of the following error, this is caused due \u starts an eight-character Unicode escape, such as \u.data
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 67-68: truncated \uXXXX escape
# it can be easily fixed with the help of '/u.data' instead of '\u.data'
ratings = pd.read_csv('path/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1") # take the first 3 columns from the 'u.data' file

# dataframe for movies
m_cols = ['movie_id', 'title'] # our new dataFrame will have 2 columns
movies = pd.read_csv('path/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")# take the first 2 columns from the 'u.item' file

# merge the two dataframes
# [movie_id, title, user_id, rating]
ratings = pd.merge(movies, ratings)

# create a new data frame with index as user_id, all the columns as '(movie)title' and each cell's value will the rating given by the user
# NaN represents that the user didn't rate it
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# builtin corr function will find correlation score for every column pair based on userRating
corrMatrix = userRatings.corr()

# corr function can take parameters
# there are different methods
# method : {‘pearson’, ‘kendall’, ‘spearman’}
# pearson : standard correlation coefficient
# kendall : Kendall Tau correlation coefficient
# spearman : Spearman rank correlation
corrMatrix = userRatings.corr(method='pearson', min_periods=100) # consider scores that are backed up by atleast 100 people

getRatings = userRatings.loc[0].dropna() # get ratings of an user

# The Series is the datastructure for a single column of a DataFrame, not only conceptually, but literally i.e. the data in a DataFrame is actually stored in memory as a collection of Series. 
simCandidates = pd.Series()
for i in range(0, len(getRatings.index)):
    # print ("Adding sims for " + getRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[getRatings.index[i]].dropna()
    # print (sims)
    # Now scale its similarity by how well I rated this movie
    # Logic: the values of all movies that are rated by the user in the correlation matrix are scaled by the rating given by user to that movie
    sims = sims.map(lambda x: x * getRatings[i])
    # print (sims)
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
# print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False) # sort the results
# print (simCandidates.head(10))

# use groupby() to add together the scores from movies that show up more than once
simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)

# filter out movies that the user already rated
filteredSims = simCandidates.drop(myRatings.index)
filteredSims.head(10) # top 10 recommended movies

