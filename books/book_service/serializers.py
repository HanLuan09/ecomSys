from rest_framework import serializers
from .models import Category, Book, Publisher, Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['publisher_id' ,'name', 'address', 'email', 'phone_number', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['book_id', 'name', 'author', 'image', 'price', 'sale', 'quantity', 
                  'des', 'category_id','authors', 'publisher']
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        publisher = validated_data.pop('publisher', None)
        authors_data = validated_data.pop('authors', [])
        # image = validated_data.pop('image', None)
        # request = self.context.get('request')

        if category_id:
            category_instance = Category.objects.filter(is_active__in=[True], category_id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')
        
        if publisher:
            publisher_id = publisher.publisher_id
            publisher_instance = Publisher.objects.filter(is_active__in=[True], publisher_id=publisher_id).first()
            if publisher_instance:
                validated_data['publisher'] = publisher_instance
            else:
                raise serializers.ValidationError('Publisher does not exist')
            
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            author_id = author_data.author_id
            author_instance = Author.objects.filter(is_active__in=[True], author_id=author_id).first()
            if author_instance:
                book.authors.add(author_instance)
            else: 
                raise serializers.ValidationError(f'Author with id {author_id} does not exist')
            
        # return Book.objects.create(image=request.FILES.get('image'), **validated_data)
        return book
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    

class BookInfoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    publisher = PublisherSerializer()
    # authors = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['book_id', 'name', 'author', 'image', 'price', 'sale', 'quantity', 'type', 
                  'des', 'category', 'publisher']

class UpdateBookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['image', 'price', 'sale', 'quantity', 'des', 'category_id', "publisher"]

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
        
        publisher = validated_data.pop('publisher', None)
        if publisher:
            publisher_id = publisher.publisher_id
            publisher_instance = Publisher.objects.filter(is_active__in=[True], publisher_id=publisher_id).first()
            if publisher_instance:
                validated_data['publisher'] = publisher_instance
            else:
                raise serializers.ValidationError('Publisher does not exist')
            
        instance.des = validated_data.get('des')

        instance.save()
        return instance
