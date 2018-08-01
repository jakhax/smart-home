from django.shortcuts import render
from .models import Device,DeviceTypes,Music
from django.core.serializers import serialize
from django.http import HttpResponse
from .utils import get_home_data,serialize_devices
import json
from decouple import config
from  forecastiopy import *

def get_room_by_id(request,room_id):
    devices=Device.get_devices_by_id(int(room_id))
    data=serialize('json',devices)
    return HttpResponse(data,content_type="json")


def get_device_type_by_id(request,device_id):
    device=DeviceTypes.objects.filter(pk=int(device_id))
    data=serialize('json',device)
    return HttpResponse(data,content_type="json")

def get_all_rooms_devices(request):
    devices=Device.objects.all()
    jdata=serialize_devices(devices)
    return HttpResponse(jdata,content_type="json")

def get_all_device_type(request):
    device=DeviceTypes.objects.all()
    data=serialize('json',device)
    return HttpResponse(data,content_type="json")

def api_get_rooms_data(request):
    data=get_home_data()
    myrooms=[{"id":i["id"],"name":i['name']['text']} for i in data["rooms"]]
    rooms=json.dumps(myrooms)
    return HttpResponse(rooms,content_type="json")
    

def get_all_music(request):
    songs=Music.objects.all()
    songs=[{"name":i.name,"url":i.music.url[1:]} for i in songs]
    data=json.dumps(songs)
    return HttpResponse(data,content_type="json")

	
def get_daily_data(request):
    town = [-1.3,36.82]
    api_key=config('API_KEY')
    fio = ForecastIO.ForecastIO(api_key, latitude=town[0], longitude=town[1])
    current = FIOCurrently.FIOCurrently(fio)
    data = {'humidity': current.humidity,'temperature': current.temperature,'pressure':current.pressure,'cloudCover':current.cloudCover,'windSpeed':current.windSpeed}

    return HttpResponse(json.dumps(data),content_type="json")


    # , 'cloudCover', 'currently', 'dewPoint', 'get', 'humidity', 
    # 'icon', 'ozone', 'precipIntensity', 'precipProbability', , 
    # 'summary', 'temperature', 'time', 'uvIndex', 'visibility', 'windBearing', 'windGust', 'windSpeed']
