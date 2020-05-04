import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_from_index(index, df):
	return df[df.index == index]["title"].values[0].capitalize()


def get_index_from_title(title, df):
	try:
		return df[df.title == title]["index"].values[0]
	except Exception as e:
		return False 


def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:", row)


def read_dataset():
	df = pd.read_csv("movies/common/movie_dataset.csv", engine='python')
	features = ['keywords','cast','genres','director']
	for feature in features:
		df[feature] = df[feature].fillna('')
	df["combined_features"] = df.apply(combine_features,axis=1)

	cv = CountVectorizer()
	count_matrix = cv.fit_transform(df["combined_features"])
	cosine_sim = cosine_similarity(count_matrix) 
	return cosine_sim, df


def movie_recommendation(movie='avatar'):
	cosine_sim, df = read_dataset()
	movie_user_likes =  movie
	movie_index = get_index_from_title(movie_user_likes, df)
	if not movie_index:
		return False
	similar_movies =  list(enumerate(cosine_sim[movie_index]))
	sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1],reverse=True)[1:]
	result = []
	i=0
	for element in sorted_similar_movies:
		result.append(get_title_from_index(element[0], df))
		i=i+1
		if i>10:
			break
	print(result)
	return result