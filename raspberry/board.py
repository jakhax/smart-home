import RPi.GPIO as GPIO
from raspberry.models import GPIO_pins
class Raspberry:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pins=GPIO_pins.objects.all()
        self.modes={"OUT":GPIO.OUT,"IN":GPIO.IN}
        self.states={False:GPIO.HIGH,True:GPIO.LOW}
        for x in self.pins:
            #setup all pins
            GPIO.setup(x.pin,self.modes[x.gpio_state])
            #restore initial state of pins
            GPIO.output(x.pin,self.states[x.default_state])
        # map(lambda x:GPIO.setup(x.pin,self.modes[x.gpio_state]),self.pins)
        # map(lambda x: GPIO.output(x.pin,self.states[x.default_state]),self.pins)
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
                GPIO.output(selected_pin.pin,self.states[pin_state])
                selected_pin.default_state=pin_state
                selected_pin.save()
                self.update_pins()
                return True
            except Exception as e:
                print(e)
                return False
        return False
