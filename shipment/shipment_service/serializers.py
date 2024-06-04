from rest_framework import serializers

from shipment_service.models import Carriers, Shipment, ShipmentInfo, Transaction

class ShipmentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentInfo
        fields = ['fname', 'lname', 'email', 'mobile', 'address', 'is_active']
    
    def update(self, instance, validated_data):
        instance.fname = validated_data.get('fname')
        instance.lname = validated_data.get('lname')
        instance.email = validated_data.get('email')
        instance.mobile = validated_data.get('mobile')
        instance.address = validated_data.get('address')

        instance.save()
        return instance

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'coefficient', 'is_active', 'des']
    
    def update(self, instance, validated_data):
        instance.coefficient = validated_data.get('coefficient')
        instance.des = validated_data.get('des')

        instance.save()
        return instance
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class CarriersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriers
        fields = ['name', 'price', 'address', 'is_active', 'email', 'mobile', 'des']
    
    def update(self, instance, validated_data):
        instance.price = validated_data.get('price')
        instance.address = validated_data.get('address')
        instance.mobile = validated_data.get('mobile')
        instance.email = validated_data.get('email')
        instance.des = validated_data.get('des')

        instance.save()
        return instance

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['order_id', 'shipment_status', 'transaction', 'payment_status', 'shipment_info', 'carrier']
    
    def create(self, validated_data):
        shipment_info = validated_data.pop('shipment_info', None)
        transaction = validated_data.pop('transaction', None)
        carrier = validated_data.pop('carrier', None)
        
        shipment_info_id = shipment_info.id
        shipment_info_instance = ShipmentInfo.objects.filter(is_active = True, pk=shipment_info_id).first()
        if shipment_info_instance:
            validated_data['shipment_info'] = shipment_info_instance
        else:
            raise serializers.ValidationError('ShipmentInfo does not exist')
            
        transaction_id = transaction.id
        transaction_instance = Transaction.objects.filter(is_active = True, pk=transaction_id).first()
        if transaction_instance:
            validated_data['transaction'] = transaction_instance
        else:
            raise serializers.ValidationError('Transaction does not exist')
        
        carrier_id = carrier.id
        carrier_instance = Carriers.objects.filter(is_active = True, pk=carrier_id).first()
        if carrier_instance:
            validated_data['carrier'] = carrier_instance
        else:
            raise serializers.ValidationError('Carrier does not exist')
        
        return Shipment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.shipment_status = validated_data.get('shipment_status')
        instance.payment_status = validated_data.get('payment_status')

        instance.save()
        return instance
