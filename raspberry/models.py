from django.db import models

from raspberry.utils import get_gpio_pins

# Create your models here.

class GPIO_pins(models.Model):
    GPIO_STATE=[("OUT","OUT"),("IN","IN")]
    PINS=[tuple((i,i)) for i in get_gpio_pins()]
    pin=models.PositiveIntegerField(choices=PINS)
    gpio_state=models.CharField(choices=GPIO_STATE,blank=True, max_length=200)
    default_state=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="GPIO pins"

    def __str__(self):
        return 'pin {} {}'.format(self.pin,self.gpio_state)

    


