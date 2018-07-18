from django.shortcuts import render
from rooms.models import Device
from django.http import HttpResponse
import json

def api_change_device_state(request,device_id):
    device=Device.objects.get(pk=int(device_id))
    device.state=not device.state
    device.save()
    return HttpResponse(json.dumps({"state":device.state}),content_type="json")