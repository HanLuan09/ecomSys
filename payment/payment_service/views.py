from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Payment, PaymentMethod
from .serializer import PaymentMethodSerializer, PaymentSerializer

class PaymentMethodView(APIView):
    def post(self, request):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, id):
        try:
            payment_method = PaymentMethod.objects.get(pk=id)
        except PaymentMethod.DoesNotExist:
            return Response({'error': 'PaymentMethod not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaymentMethodSerializer()
        serializer.destroy(payment_method)
        return Response({'message': 'PaymentMethod soft deleted'}, status=status.HTTP_204_NO_CONTENT)

class PaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            payment = Payment.objects.get(pk=id)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)