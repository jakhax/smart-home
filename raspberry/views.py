from django.shortcuts import render
from django.conf import settings
from rooms.models import Device
from django.http import HttpResponse
import json
from raspberry.models import GPIO_pins

#board setup
if settings.IS_PI:
    from raspberry.board import Raspberry

else:
    class Raspberry:
        def __init__(self):
            self.pins=GPIO_pins.objects.all()
        def valid_pin(self,pid):
            return True if pid in [i.pk for i in self.pins] else False
        def update_pins(self):
            self.pins=GPIO_pins.objects.all()
        def get_pin_state(self,pk):
            if self.valid_pin(pk):
                return GPIO_pins.objects.get(pk=pk).default_state           
        def toggle_pin(self,pid):
            if self.valid_pin(pid):
                selected_pin=GPIO_pins.objects.get(pk=pid)
                pin_state= not selected_pin.default_state
                try:
                    selected_pin.default_state=pin_state
                    selected_pin.save()
                    self.update_pins()
                    print("path")
                    return True
                except Exception as e:
                    print(e)
                    return False
            return False

#lets create a pi object
raspberry=Raspberry()


def api_change_device_state(request,device_id):
    device=Device.objects.get(pk=int(device_id))
    gpio_pin=device.pin
    if raspberry.toggle_pin(gpio_pin.pk):
        state=raspberry.get_pin_state(gpio_pin.pk)
    return HttpResponse(json.dumps({"state":state}),content_type="json")
