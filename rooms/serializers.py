from rooms.models import Device,DeviceTypes

def get_device_types():
    device_types=list(DeviceTypes.objects.all())
    dt={}
    for i in device_types:
        dt[i.pk]={"name":i.name,"iconclass":i.iconclass,"style_type":i.style_type}
    return dt

def serialize_devices():
    devices=list(Device.objects.all())
    device_types=get_device_types()
    nDevices=[{"id":i.id,"device_type":device_types[i.device_type.id],"room":i.room,"name":i.name,"state":i.pin.default_state} for i in devices]
    return nDevices

