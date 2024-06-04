from rest_framework import serializers

from payment_service.models import Payment, PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['name', 'is_active']
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order_id', 'date_paymented', 'total', 'payment_method', 'status']

    def create(self, validated_data):
        payment_method = validated_data.pop('payment_method', None)
        payment_method_id = payment_method.id
        payment_method_instance = PaymentMethod.objects.filter(is_active = True, pk=payment_method_id).first()
        if payment_method_instance:
            validated_data['payment_method'] = payment_method_instance
        else:
            raise serializers.ValidationError('PaymentMethod does not exist')
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('tatus')

        instance.save()
        return instance