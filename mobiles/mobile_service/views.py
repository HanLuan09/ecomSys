import requests
from djongo.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Mobile
from .serializers import CategorySerializer, ProducerSerializer, MobileSerializer, MobileInfoSerializer, UpdateMobileSerializer

class CreateCategoryView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateProducerView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = ProducerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class AddMobileView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = MobileSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(is_active__in=[True]).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MobileListView(APIView):
    def get(self, request):
        mobiles = Mobile.objects.filter(is_active__in=[True]).all()
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MobileListofCategoryView(APIView):
    def get(self, request, category_id):
        mobiles = Mobile.objects.filter(category_id=category_id, is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchMobileListView(APIView):
    def get(self, request, key):
        mobiles = Mobile.objects.filter(Q(name__icontains=key), is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateMobileView(APIView):
    def put(self, request, mobile_id):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(mobile_id=mobile_id)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateMobileSerializer(mobile, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteCategory(APIView):
    def delete(self, request, category_id):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                category = Category.objects.get(category_id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = CategorySerializer()
            serializer.destroy(category)
            
            return Response({'message': 'Category soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteMobile(APIView):
    def delete(self, request, mobile_id):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(mobile_id=mobile_id)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = MobileSerializer()
            serializer.destroy(mobile)
            
            return Response({'message': 'Mobile soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class MobileDetailView(APIView):
    def get(self, request, mobile_id):
        mobile = Mobile.objects.filter(mobile_id=mobile_id, is_active__in=[True]).first()
        serializer = MobileInfoSerializer(mobile)
        return Response(serializer.data, status=status.HTTP_200_OK)