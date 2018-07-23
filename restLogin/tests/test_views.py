from django.test import TestCase
from django.test.utils import override_settings
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

import unittest
from calendar import timegm
from datetime import datetime, timedelta
import time

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
from django import get_version

User = get_user_model()

orig_datetime = datetime


class BaseTestCase(TestCase):

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


class TestCustomResponsePayload(BaseTestCase):
    def setUp(self):
        self.original_handler = views.jwt_response_payload_handler
        return super(TestCustomResponsePayload, self).setUp()

    def test_jwt_login_custom_response_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """
        client = APIClient(enforce_csrf_checks=True)
        response = client.post('/auth-token/',format='json')
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        views.jwt_response_payload_handler = self.original_handler



class ObtainJSONWebTokenTests(BaseTestCase):
    def test_jwt_login_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """
        client = APIClient(enforce_csrf_checks=True)
        response = client.post('/auth-token/', format='json')

        self.assertTrue(response.status_code, status.HTTP_200_OK)


    
    def test_jwt_login_json_bad_creds(self):
        """
        Ensure JWT login view using JSON POST fails
        if bad credentials are used.
        """
        client = APIClient(enforce_csrf_checks=True)

        self.data['password'] = 'wrong'
        response = client.post('/auth-token/', format='json')

        self.assertTrue(response.status_code, 400)



    def test_jwt_login_json_missing_fields(self):
        """
        Ensure JWT login view using JSON POST fails if missing fields.
        """
        client = APIClient(enforce_csrf_checks=True)

        response = client.post('/auth-token/',
                               {'username': self.username}, format='json')

        self.assertTrue(response.status_code, 400)



    def test_jwt_login_form(self):
        """
        Ensure JWT login view using form POST works.
        """
        client = APIClient(enforce_csrf_checks=True)
        response = client.post('/auth-token/', self.data)

        # decoded_payload = utils.jwt_decode_handler(response.data['token'])

        self.assertTrue(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(decoded_payload['username'], self.username)

    # def test_jwt_login_with_expired_token(self):
    #     """
    #     Ensure JWT login view works even if expired token is provided
    #     """
    #     payload = utils.jwt_payload_handler(self.user)
    #     payload['exp'] = 1
    #     token = utils.jwt_encode_handler(payload)

    #     auth = 'JWT {0}'.format(token)
    #     client = APIClient(enforce_csrf_checks=True)
    #     response = client.post(
    #         '/auth-token/', self.data,
    #         HTTP_AUTHORIZATION=auth, format='json')

    #     decoded_payload = utils.jwt_decode_handler(response.data['token'])

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertFalse(decoded_payload['username'], self.username)

    # def test_jwt_login_using_zero(self):
    #     """
    #     Test to reproduce issue #33
    #     """
    #     client = APIClient(enforce_csrf_checks=True)

    #     data = {
    #         'username': '0',
    #         'password': '0'
    #     }

    #     response = client.post('/auth-token/', data, format='json')

    #     self.assertTrue(response.status_code, 400)

