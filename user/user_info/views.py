from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_service.models import UserProfile, UserAddress
from user_service.authentication import SafeJWTAuthentication
from user_service.serializers import UpdateProfileSerializer, UserInfoSerializer, UserProfileSerializer, UserAddressSerializer, UserAddressInfoSerializer, UpdateAddressSerializer
from rest_framework.permissions import IsAuthenticated

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SafeJWTAuthentication]

    def get(self, request):
        user = request.user
        user_serializer = UserInfoSerializer(user)
        user_profile = UserProfile.objects.filter(is_active=True, user=user).first()

        if user_profile:
            profile_serializer = UserProfileSerializer(user_profile)
            user_data = user_serializer.data
            user_data['user_profile'] = profile_serializer.data
        else:
            user_data = user_serializer.data
            user_data['user_profile'] = None

        return Response(user_data, status=status.HTTP_200_OK)
    

    
class CreateUserProfile(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # serializer = UserProfileSerializer(data=request.data)
        serializer = UserProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        # Lấy UserProfile của user hiện tại
        user_profile = UserProfile.objects.get(user=request.user)
        # Tạo serializer với instance là UserProfile và data là request.data
        serializer = UpdateProfileSerializer(instance=user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateUserAddress(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = UserAddressSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAddressInfoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SafeJWTAuthentication]

    def get(self, request):
        user = request.user
        user_addresses = UserAddress.objects.filter(user=user)
        serializer = UserAddressInfoSerializer(user_addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateAddressView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        # Lấy UserProfile của user hiện tại
        user_address = UserAddress.objects.get(user=request.user)
        serializer = UpdateAddressSerializer(instance=user_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
