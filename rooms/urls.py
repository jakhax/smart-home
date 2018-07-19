from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api-get-room/(?P<room_id>\d+)$',views.get_room_by_id,name='get-room'),
    url(r'^api-get-rooms-devices$',views.get_all_rooms_devices,name='get-all-rooms-devices'),
    url(r'^api-get-all-device-types$',views.get_all_device_type,name='get-all-device-types'),
    url(r'^api-get-device-type/(?P<device_id>\d+)$',views.get_device_type_by_id,name='get-device-type'),
     url(r'^api-get-room-data$',views.api_get_rooms_data,name='get-room-data'),
]