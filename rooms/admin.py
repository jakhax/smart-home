from django.contrib import admin

# Register your models here.
from  .models import Device,DeviceTypes

admin.site.register(
    
        Device,
        list_display=["name","room","state","pin"]

)

admin.site.register(
        DeviceTypes,
        list_display=["name","iconclass","style_type"]
        )