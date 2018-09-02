from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api-get-smart-home-info$',views.get_smart_home_info,name='get-smart-home-info'),
    url(r'^api-get-music$',views.get_all_music,name='get-all-music'),
    url(r'^api-get-daily-data$',views.get_daily_data,name='get-daily-data'), 
]
