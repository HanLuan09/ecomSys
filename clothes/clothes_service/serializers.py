from rest_framework import serializers
from .models import Category, Clothes, Producer, Style

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['style_id' ,'name', 'des']
        
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

class ClothesSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Clothes
        fields = ['clothes_id', 'name', 'image', 'price', 'sale', 'quantity', 'des', 
                  'category_id', 'style', 'producer']
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        style = validated_data.pop('style', None)
        producer = validated_data.pop('producer', None)
        print(producer)
        # image = validated_data.pop('image', None)
        # request = self.context.get('request')

        if category_id:
            category_instance = Category.objects.filter(is_active__in=[True], category_id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')
            
        if style:
            style_id = style.style_id
            style_instance = Style.objects.filter(is_active__in=[True], style_id=style_id).first()
            if style_instance:
                validated_data['style'] = style_instance
            else:
                raise serializers.ValidationError('Style does not exist')
        
        if producer:
            producer_id = producer.producer_id
            producer_instance = Producer.objects.filter(is_active__in=[True], producer_id=producer_id).first()
            if producer_instance:
                validated_data['producer'] =  producer_instance
            else:
                raise serializers.ValidationError('Producer does not exist')
        
        return Clothes.objects.create(**validated_data)
        #return Clothes.objects.create(image=request.FILES.get('image'), **validated_data)
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    

class ClothesInfoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    style = StyleSerializer()
    producer = ProducerSerializer()
    class Meta:
        model = Clothes
        fields = ['clothes_id', 'name', 'image', 'price', 'sale', 'quantity', 
                  'type', 'des', 'category', 'style', 'producer']

class UpdateClothesSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Clothes
        fields = ['image', 'price', 'sale', 'quantity', 'des', 'category_id', 'style_id', 'producer_id']

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
        
        style_id = validated_data.pop('style_id', None)
        style_instance = Style.objects.filter(is_active__in=[True], style_id=style_id).first()
        if style_instance:
            instance.style = style_instance
        else:
            raise serializers.ValidationError('Style does not exist')
        
        producer_id = validated_data.pop('producer_id', None)
        producer_instance = Producer.objects.filter(is_active__in=[True], producer_id=producer_id).first()
        if producer_instance:
            instance.producer = producer_instance
        else:
            raise serializers.ValidationError('Producer does not exist')

        instance.des = validated_data.get('des')

        instance.save()
        return instance
