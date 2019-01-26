from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated,AllowAny
import jwt
from smart_home.settings import SECRET_KEY

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class LoginUserView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        # @test: curl -X POST -H "Content-Type: application/json" \
        # -d '{"username":"username","password":"pass"}' http://localhost:8000/api-login-user/
        username = request.data.get('username')
        password = request.data.get('password')
        self.request_validation = self.validate_user(request)
        if self.request_validation:
            payload= jwt_payload_handler(self.user)
            token = {
                'token': jwt.encode(payload, SECRET_KEY),
                'status': 'success'
                }  
            return Response(token)
        return Response({'error': 'Invalid credentials'}, status=401)

    def validate_user(self,r):
        self.username = r.data.get("username")
        self.password = r.data.get("password")
        try:
            self.user= authenticate(username=self.username,password=self.password)
            if self.user:
                return True
        except:
            return False

class PasswordReset(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        if request.user.username=="testuser":
            return Response({'error': 'Bad request'}, status=400)
        self.u=User.objects.get(pk=request.user.pk)
        self.post_data=request.data
        if self.change_password():
            return Response({'success': 'success'})
        return Response({'error': 'Bad request'}, status=400)

    def change_password(self):
        try:
            if len(self.post_data.get("password")) > 0 and self.post_data.get("password")==self.post_data.get("confirmPassword"):
                self.password=self.post_data.get("password")
                self.u.set_password(self.password)
                self.u.save()
                return True
            return False
        except Exception as err:
            print(err)
            return False


def print_headers(request):
    import re
    regex = re.compile('^HTTP_')
    headers=dict((regex.sub('', header), value) for (header, value) 
        in request.META.items() if header.startswith('HTTP_'))
    print(headers)