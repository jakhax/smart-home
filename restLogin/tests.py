from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .views import LoginUserView

import rest_framework
import django
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt import utils
import unittest
from django.test.utils import override_settings
from distutils.version import StrictVersion

drf2 = rest_framework.VERSION < StrictVersion('3.0.0')
drf3 = rest_framework.VERSION >= StrictVersion('3.0.0')




User = get_user_model()

# Create your tests here.
class LoginUser(APITestCase):
    # urlpatterns = [
    #     path((r'^',include(('restLogin.urls','restLogin'),namespace="rest-login")),
    #     ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        data = {'name': 'Washere'}
        response = self.client.post( data, format='json')
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'Washere')

class JSONWebTokenSerializerTests(TestCase):
    def setUp(self):
        self.email = 'sarah@example.com'
        self.username = 'sarah'
        self.password = 'password'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }


    def test_empty_drf2(self):
        serializer = JSONWebTokenSerializer()
        expected = {
            'username': ''
        }

        self.assertTrue(serializer.data, expected)


    def test_create(self):
        serializer = JSONWebTokenSerializer(data=self.data)
        is_valid = serializer.is_valid()

        token = serializer.object['token']
        decoded_payload = utils.jwt_decode_handler(token)

        self.assertTrue(is_valid)
        self.assertEqual(decoded_payload['username'], self.username)

    def test_invalid_credentials(self):
        self.data['password'] = 'wrong'
        serializer = JSONWebTokenSerializer(data=self.data)
        is_valid = serializer.is_valid()

        expected_error = {
            'non_field_errors': ['Unable to log in with provided credentials.']
        }

        self.assertFalse(is_valid)
        self.assertEqual(serializer.errors, expected_error)

    
    def test_disabled_user(self):
        self.user.is_active = False
        self.user.save()

        serializer = JSONWebTokenSerializer(data=self.data)
        is_valid = serializer.is_valid()

        expected_error = {
            'non_field_errors': ['User account is disabled.']
        }

        self.assertFalse(is_valid)
        self.assertTrue(serializer.errors, expected_error)


    @override_settings(AUTHENTICATION_BACKENDS=[
        'django.contrib.auth.backends.AllowAllUsersModelBackend'])
    def test_disabled_user_all_users_backend(self):
        self.user.is_active = False
        self.user.save()

        serializer = JSONWebTokenSerializer(data=self.data)
        is_valid = serializer.is_valid()

        expected_error = {
            'non_field_errors': ['User account is disabled.']
        }

        self.assertFalse(is_valid)
        self.assertEqual(serializer.errors, expected_error)

    def test_required_fields(self):
        serializer = JSONWebTokenSerializer(data={})
        is_valid = serializer.is_valid()

        expected_error = {
            'username': ['This field is required.'],
            'password': ['This field is required.']
        }

        self.assertFalse(is_valid)
        self.assertEqual(serializer.errors, expected_error)