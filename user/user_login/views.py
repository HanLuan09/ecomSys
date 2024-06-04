from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_service.authentication import SafeJWTAuthentication
from user_service.utils import generate_access_token, generate_refresh_token
from user_service.serializers import ChangePasswordSerializer, UserInfoSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  
            access_token = generate_access_token(user)
            refresh_token = generate_refresh_token(user)

            user_serializer = UserInfoSerializer(user)
            
            return Response({
                'user': user_serializer.data,
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)