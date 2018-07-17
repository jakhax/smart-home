from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api-change-device-state/(?P<device_id>\d+)$',views.api_change_device_state,name='change-device-state'),   
]