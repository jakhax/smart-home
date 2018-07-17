from django.contrib import admin

# Register your models here.
from .models import GPIO_pins

admin.site.register(
        GPIO_pins,
        list_display=["pin","gpio_state","default_state"]
        )