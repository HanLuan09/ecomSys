from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shipment_service.models import Carriers, Shipment, ShipmentInfo, Transaction
from shipment_service.serializers import CarriersSerializer, ShipmentInfoSerializer, ShipmentSerializer, TransactionSerializer

class ShipmentInfoView(APIView):
    def post(self, request):
        serializer = ShipmentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            shipment_info = ShipmentInfo.objects.get(pk=id)
        except ShipmentInfo.DoesNotExist:
            return Response({'error': 'ShipmentInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShipmentInfoSerializer(shipment_info ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            shipment_info = ShipmentInfo.objects.get(pk=id)
        except ShipmentInfo.DoesNotExist:
            return Response({'error': 'ShipmentInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShipmentInfoSerializer()
        serializer.destroy(shipment_info)
        
        return Response({'message': 'ShipmentInfo soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class TransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            transaction = Transaction.objects.get(pk=id)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            transaction = Transaction.objects.get(pk=id)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransactionSerializer()
        serializer.destroy(transaction)
        return Response({'message': 'Transaction soft deleted'}, status=status.HTTP_204_NO_CONTENT)

class CarriersView(APIView):
    def post(self, request):
        serializer = CarriersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            carrier = Carriers.objects.get(pk=id)
        except Carriers.DoesNotExist:
            return Response({'error': 'Carrier not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarriersSerializer(carrier ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            carrier = Carriers.objects.get(pk=id)
        except Carriers.DoesNotExist:
            return Response({'error': 'Carrier not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarriersSerializer()
        serializer.destroy(carrier)
        return Response({'message': 'Carrier soft deleted'}, status=status.HTTP_204_NO_CONTENT)

class ShipmentView(APIView):
    def post(self, request):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            shipment = Shipment.objects.get(pk=id)
        except Shipment.DoesNotExist:
            return Response({'error': 'Shipment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShipmentSerializer(shipment ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
