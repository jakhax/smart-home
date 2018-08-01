from django.db import models
import json
from . import utils
from raspberry.models import GPIO_pins
# Create your models here.

class DeviceTypes(models.Model):
    STYLES=(("primary","primary"),("info","info"),("success","success"),("danger","danger"),("warning","warning"))
    ICONS=[tuple((i,i)) for i in utils.get_nb_icons() ]
    name=models.CharField(max_length=255,blank=True, null=True)
    iconclass=models.CharField(choices=ICONS,max_length=255,blank=True, null=True)
    style_type=models.CharField(choices=STYLES,max_length=255,blank=True, null=True)

    class Meta:
        verbose_name_plural = "DeviceTypes"

    def __str__(self):
        return "{}".format(self.name)
    


class Device(models.Model):
    CHOICES=[tuple((i,i)) for i in utils.get_rooms() ]
    device_type=models.ForeignKey(DeviceTypes, on_delete=models.CASCADE,blank=True, null=True)
    room=models.CharField(choices=CHOICES,max_length=255,blank=True)
    name=models.CharField(max_length=255,unique=True,blank=True)  
    pin  = models.OneToOneField(GPIO_pins, on_delete=models.PROTECT,blank=True,null=True)                                                                                                                                                                                
    # state=models.BooleanField(default=False)

    @classmethod
    def get_room_by_id(cls,room_id):
        data=utils.get_home_data()
        return data["rooms"][room_id]

    @classmethod
    def get_devices_by_id(cls,room_id):
        data=utils.get_home_data()
        return cls.objects.filter(room=data["rooms"][room_id]['name']['text'])
        

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural="Devices"
    

class Music(models.Model):
    name=models.CharField(max_length=255,unique=True,blank=True) 
    music= models.FileField(upload_to = u'mp3/', max_length=200)

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        verbose_name_plural="Music"