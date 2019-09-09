from bs4 import BeautifulSoup
import requests
from rest_framework.decorators import api_view
from kino_kz.models import Movie, ComingSoonMovie
from kino_kz.serializers import MovieSerializer, ComingSoonMovieSerializer
from rest_framework.response import Response
import datetime


def delete_everything(Data):
    Data.objects.all().delete()


def scrape_movies(url, Data):
    delete_everything(Data)
    request = requests.get(url)
    html_doc = request.text
    soup = BeautifulSoup(html_doc, "html.parser")
    movie_descriptions = soup.find_all('div', {'class': 'movie_description'})

    cnt = 0
    images = []

    posters = soup.find_all('div', {'class': 'movie_poster'})
    for poster in posters:
        image = str(poster.findAll('img')[0])
        image = image.split('src="')
        image = image[1].split('"')[0]
        if image[0] == '/':
            image = 'https://sun9-28.userapi.com/c850120/v850120013/1cd586/ALTpNEePl4c.jpg'
            # image = 'http://kino.kz/images/def/320x222.jpg'
        images.append(image)

    counter = cnt

    for item in movie_descriptions:
        premiere = item.find('span').text
        premiere = premiere.split('-')
        if premiere[0][0] == 'С':
            premiere[0] = premiere[0][2:]
            premiere_date = premiere[2] + ' ' + premiere[1] + ' ' + premiere[0]
            premiere_date = datetime.datetime.strptime(premiere_date, '%Y %b %d')
        else:
            premiere_date = datetime.datetime.now()

        title = item.find_all('dt')[1].text
        genre = item.find_all('dt')[2].text
        description = item.find_all('dt')[3].text
        age_string = item.find('div', {'class': 'prim_age'})
        if age_string is not None:
            age = int(''.join(filter(str.isdigit, age_string.text)))
        else:
            age = 0

        if Data.objects.filter(title=title).exists() == False:
            movie = Data.objects.create(id=cnt, title=title, genre=genre, premiere=premiere_date,
                                        description=description, age=age, poster=images[cnt - counter])
            cnt += 1


@api_view(['GET'])
def current_movies(request):
    scrape_movies('http://kino.kz', Movie)
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def coming_soon_movies(request):
    scrape_movies('http://kino.kz/soon', ComingSoonMovie)
    if request.method == 'GET':
        movies = ComingSoonMovie.objects.all()
        serializer = ComingSoonMovieSerializer(movies, many=True)
        return Response(serializer.data)


