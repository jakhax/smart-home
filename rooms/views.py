from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Device,DeviceTypes,Music
from django.core.serializers import serialize
from .utils import get_home_data
from .serializers import serialize_devices
from decouple import config
from  forecastiopy import *


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_smart_home_info(request):
    data={"rooms":[]}
    data["devices"]=serialize_devices()
    for r in get_home_data()["rooms"]:
        data["rooms"].append({"id":r["id"],"name":r['name']['text']})
    return Response(data)
   

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_all_music(request):
    songs=Music.objects.all()
    songs=[{"name":i.name,"url":i.music.url[1:]} for i in songs]
    return Response(songs)

	
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_daily_data(request):
    town = [-1.3,36.82]
    api_key=config('WEATHER_API_KEY')
    fio = ForecastIO.ForecastIO(api_key, latitude=town[0], longitude=town[1])
    current = FIOCurrently.FIOCurrently(fio)
    data = {'humidity': current.humidity,'temperature': current.temperature,
            'pressure':current.pressure,'cloudCover':current.cloudCover,'windSpeed':current.windSpeed}
    return Response(data)

