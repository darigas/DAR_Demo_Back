from bs4 import BeautifulSoup
import requests
from rest_framework.decorators import api_view
from kino_kz.models import Cinema, City
from kino_kz.serializers import CinemaSerializer, CitySerializer
from rest_framework.response import Response


def delete_everything(Data):
    Data.objects.all().delete()


def scrape_cinemas(url, cnt, data):
    request = requests.get(url)
    html_doc = request.text
    soup = BeautifulSoup(html_doc, "html.parser")
    movie_description = soup.find('table', {'class': 'about-cinema'})
    try:
        st = str(movie_description.text)
        st = st.split('\n')
        print (st)
        title = st[3]
        address = st[7]
        phone = st[12]
        description = st[17]
        image = 'http://s.kino.kz/images/cinemas/' + str(cnt) + '.jpg'
        data.objects.create(id=cnt, title=title, address=address, phone=phone, description=description, poster=image)
    except Exception as e:
        return


@api_view(['GET'])
def cinemas(request):
    delete_everything(Cinema)
    for i in range(170):
        scrape_cinemas('http://kino.kz/cinema/' + str(i), i, Cinema)
    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_cities(request):
    if request.method == "GET":
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_cinemas(request):
    if request.method == "GET":
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_city_cinemas(request, city):
    if request.method == "GET":
        # Аксай
        if city == 'aksay':
            city = "Аксай"
        # Аксу
        elif city == "aksu":
            city = "Аксу"
        # Актау
        elif city == "aktau":
            city = "Актау"
        # Актобе
        elif city == "aktobe":
            city = "Актобе"
        # Алматы
        elif city == "almaty":
            city = "Алматы"
        # Атырау
        elif city == "atyrau":
            city = "Атырау"
        # Бурыл
        elif city == "buryl":
            city = "Бурыл"
        # Жанаозен
        elif city == "zhanaozen":
            city = "Жанаозен"
        # Жаркент
        elif city == "zharkent":
            city = "Жаркент"
        # Житикара
        elif city == "zhitikara":
            city = "Житикара"
        # Караганда
        elif city == "karaganda":
            city = "Караганда"
        # Кокшетау
        elif city == "kokshetau":
            city = "Кокшетау"
        # Костанай
        elif city == "kostanay":
            city = "Костанай"
        # Кызылорда
        elif city == "kyzylorda":
            city = "Кызылорда"
        # Мерке
        elif city == "merke":
            city = "Мерке"
        # Нур-Султан
        elif city == "nur-sultan":
            city = "Нур-Султан"
        # Павлодар
        elif city == "pavlodar":
            city = "Павлодар"
        # Петропавловск
        elif city == "petropavlovsk":
            city = "Петропавловск"
        # Рудный
        elif city == "rydny":
            city = "Рудный"
        # Сатпаев
        elif city == "satpayev":
            city = "Сатпаев"
        # Семей
        elif city == "semey":
            city = "Семей"
        # Талдыкорган
        elif city == "taldykorgan":
            city = "Талдыкорган"
        # Тараз
        elif city == "taraz":
            city = "Тараз"
        # Темиртау
        elif city == "temirtau":
            city = "Темиртау"
        # Уральск
        elif city == "uralsk":
            city = "Уральск"
        # Усть-Каменогорск
        elif city == "ust-kamenogorsk":
            city = "Усть-Каменогорск"
        # Шу
        elif city == "shu":
            city = "Шу"
        # Шымкент
        elif city == "shymkent":
            city = "Шымкент"
        # Щучинск
        elif city == "shchuchinsk":
            city = "Щучинск"
        # Экибастуз
        elif city == "ekibastuz":
            city = "Экибастуз"

        cinemas = Cinema.objects.filter(address__contains=city + ',')
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)