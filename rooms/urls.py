from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api-get-room/(?P<room_id>\d+)$',views.get_room_by_id,name='get-room'),
    url(r'^api-get-device-type/(?P<device_id>\d+)$',views.get_device_type_by_id,name='get-device-type'),
]