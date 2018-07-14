from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework_jwt.views import (obtain_jwt_token,
                                        verify_jwt_token,
                                        refresh_jwt_token)
from restLogin import views


urlpatterns = [
    url(r'^api-token-auth', obtain_jwt_token),
    url(r'^api-token-refresh', refresh_jwt_token),
    url(r'^api-token-verify', verify_jwt_token),
    # url(r'^api-register-user', views.CreateUserView.as_view()),
    url(r'^api-login-user', views.LoginUserView.as_view()),
    # url(r'^(?P<path>.*\..*)$', RedirectView.as_view(url='/static/%(path)s')),
    # url(r'^', TemplateView.as_view(template_name='angular/index.html')),
]