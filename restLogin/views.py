from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
import jwt
import json

from .serializers import UserSerializer
from smart_home.settings import SECRET_KEY

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# class CreateUserView(CreateAPIView):
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             user = self.model.get(username=serializer.data['username'])
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             return Response(
#                 token,
#                 status=status.HTTP_201_CREATED,
#                 headers=headers
#             )
#         else:
#             return Response(
#                 status=status.HTTP_400_BAD_REQUEST
#             )


class LoginUserView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('email')
        password = request.data.get('password')
        print(request.data)

        user = authenticate(username=username, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = {
                'token': jwt.encode(payload, SECRET_KEY),
                'status': 'success'
                }    
            print('washere')
            return Response(token)
        else:
            return Response(
              {'error': 'Invalid credentials',
              'status': 'failed'},
            )

