from rest_framework import serializers
from .models import Category, Mobile, Producer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['producer_id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class MobileSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['mobile_id', 'name', 'image', 'price', 'sale', 'quantity', 'des', 'category_id', 'producer']
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        producer = validated_data.pop('producer', None)
        # image = validated_data.pop('image', None)
        # request = self.context.get('request')
        print(validated_data)
        print(producer)
        producer_id = producer.producer_id
        if category_id:
            category_instance = Category.objects.filter(is_active__in=[True], category_id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')
        if producer_id:
            producer_instance = Producer.objects.filter(is_active__in=[True], producer_id=producer_id).first()
            if producer_instance:
                validated_data['producer'] = producer_instance
            else:
                raise serializers.ValidationError('Producer does not exits')
        # return Mobile.objects.create(image=request.FILES.get('image'), **validated_data)
        return Mobile.objects.create(**validated_data)
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    

class MobileInfoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    producer = ProducerSerializer()
    class Meta:
        model = Mobile
        fields = ['mobile_id', 'name', 'image', 'price', 'sale', 'quantity', 'type', 
                  'des', 'category', 'producer']

class UpdateMobileSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['image', 'price', 'sale', 'quantity', 'des', 'category_id', 'producer_id']

    def update(self, instance, validated_data):
        request = self.context.get('request')

        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')

        category_id = validated_data.pop('category_id')
        category_instance = Category.objects.filter(is_active__in=[True], category_id=category_id).first()
        if category_instance:
            instance.category = category_instance
        else:
            raise serializers.ValidationError('Category does not exist')
        
        producer_id = validated_data.pop('producer_id')
        producer_instance = Producer.objects.filter(is_active__in=[True], producer_id=producer_id).first()
        if producer_instance:
            instance.producer = producer_instance
        else:
            raise serializers.ValidationError('Producer does not exist')
        
        instance.des = validated_data.get('des')

        instance.save()
        return instance
