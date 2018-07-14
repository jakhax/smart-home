from django.shortcuts import render
from .models import Device,DeviceTypes
from django.core.serializers import serialize
from django.http import HttpResponse

def get_room_by_id(request,room_id):
    devices=Device.get_devices_by_id(int(room_id))
    data=serialize('json',devices)
    return HttpResponse(data,content_type="json")


def get_device_type_by_id(request,device_id):
    device=DeviceTypes.objects.filter(pk=int(device_id))
    data=serialize('json',device)
    return HttpResponse(data,content_type="json")

