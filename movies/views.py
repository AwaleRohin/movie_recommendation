from django.shortcuts import render
from movies.common import movie_recommedation as movie_recommedation
import requests
import json
import yaml

# Create your views here.

def homepage(request):
    return render(request, 'movieUi.html')


def serach_movie(request):
    result = []
    credentials = yaml.load(open('credentials.yaml'), Loader=yaml.FullLoader)
    simliar_movies = movie_recommedation.movie_recommendation(request.GET.get('search'))
    if not simliar_movies:
        return render(request, 'similar_movie.html',{'result':result, 'message':'Sorry couldnt get the result for this movies.'}) 
    url ='http://www.omdbapi.com/?s={}&type=movie&apikey={}'
    for movie in simliar_movies:
        response = requests.get(url.format(movie,credentials['api_key']))
        if not 'Error' in response.text:
            result.append(json.loads(response.text))
    return render(request, 'similar_movie.html',{'result':result}) 