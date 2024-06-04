import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model

class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None

        try:
            token_prefix, access_token = authorization_header.split(' ')
            if token_prefix != 'Bearer':
                raise exceptions.AuthenticationFailed('Invalid token prefix')
            
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access token expired')
        except ValueError:
            raise exceptions.AuthenticationFailed('Invalid token format')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        
        user_id = payload.get('user_id')
        if user_id is None:
            raise exceptions.AuthenticationFailed('User ID not found in token payload')
        
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive')

        return (user, None)
