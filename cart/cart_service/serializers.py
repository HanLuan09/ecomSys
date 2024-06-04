from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['user_id', 'quantity', 'type', 'product_id']
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
    
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity')
        instance.save()
        return instance