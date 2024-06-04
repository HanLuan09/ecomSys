import requests
from djongo.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Clothes
from .serializers import CategorySerializer, StyleSerializer, ProducerSerializer, ClothesSerializer, ClothesInfoSerializer, UpdateClothesSerializer

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
    
class CreateStyleView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = StyleSerializer(data=request.data)
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
    
class AddClothesView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = ClothesSerializer(data=request.data, context={'request': request})
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
    
class ClothesListView(APIView):
    def get(self, request):
        clothess = Clothes.objects.filter(is_active__in=[True]).all()
        serializer = ClothesInfoSerializer(clothess, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClothesListofCategoryView(APIView):
    def get(self, request, category_id):
        clothess = Clothes.objects.filter(category_id=category_id, is_active__in=[True])
        serializer = ClothesInfoSerializer(clothess, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchClothesListView(APIView):
    def get(self, request, key):
        clothess = Clothes.objects.filter(Q(name__icontains=key), is_active__in=[True])
        serializer = ClothesInfoSerializer(clothess, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateClothesView(APIView):
    def put(self, request, clothes_id):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            try:
                clothes = Clothes.objects.get(clothes_id=clothes_id)
            except Clothes.DoesNotExist:
                return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateClothesSerializer(clothes, data=request.data, context={'request': request})
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

class DeleteClothes(APIView):
    def delete(self, request, clothes_id):
        token_verification_url = "http://localhost:4001/api/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                clothes = Clothes.objects.get(clothes_id=clothes_id)
            except Clothes.DoesNotExist:
                return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ClothesSerializer()
            serializer.destroy(clothes)
            
            return Response({'message': 'Clothes soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class ClothesDetailView(APIView):
    def get(self, request, clothes_id):
        clothes = Clothes.objects.filter(clothes_id=clothes_id, is_active__in=[True]).first()
        serializer = ClothesInfoSerializer(clothes)
        return Response(serializer.data, status=status.HTTP_200_OK)