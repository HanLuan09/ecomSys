from rest_framework import serializers

from order_service.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'type', 'price', 'sale', 'product_id']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['user_id', 'date_ordered', 'total', 'status', 'is_cancel' 'order_items']

class OrderAddSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['user_id', 'order_items']
    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        total = 0
        # Tạo đơn hàng trước khi tạo các order item
        order = Order.objects.create(**validated_data)
        # Tạo và tính tổng số tiền từ các order item
        for item_data in order_items_data:
            price = item_data['price']
            sale = item_data['sale']
            total += price * (1 - sale / 100)
            OrderItem.objects.create(order=order, **item_data)
        # Cập nhật tổng số tiền cho đơn hàng
        order.total = total
        order.save()
        return order


