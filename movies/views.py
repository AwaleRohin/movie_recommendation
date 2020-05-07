from django.shortcuts import render
from movies.common import movie_recommedation as movie_recommedation
import requests
import json
import yaml
import redis
import ast

# Create your views here.
redis = redis.Redis(host='localhost', port=6379, db=0)

def homepage(request):
    return render(request, 'movieUi.html')


def search_movie(request):
    result = []
    credentials = yaml.load(open('credentials.yaml'), Loader=yaml.FullLoader)
    simliar_movies = movie_recommedation.movie_recommendation(request.GET.get('search'))
    if not simliar_movies:
        return render(request, 'similar_movie.html',{'result':result, 'message':'Sorry couldnt get the result for this movies.'}) 
    url ='http://www.omdbapi.com/?s={}&type=movie&apikey={}'
    for movie in simliar_movies:
        cached_movie = redis.get(movie)
        if not cached_movie:
            response = requests.get(url.format(movie,credentials['api_key']))
            if not 'Error' in response.text:
                redis.setex(movie, 3060, str(response.text))
                result.append(json.loads(response.text))
        else:
            json_data = ast.literal_eval(str(cached_movie, 'utf-8'))
            result.append(json_data)
    return render(request, 'similar_movie.html',{'result':result, 'search':request.GET.get('search').capitalize()}) 
