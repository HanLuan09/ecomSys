from rest_framework import serializers
from .models import Manager
from django.contrib.auth.hashers import make_password, check_password

class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'username', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class ManagerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError('Username and password are required.')

        user = Manager.objects.filter(username=username).first()
        if user:
            if check_password(password, user.password):
                return user 
            else:
                raise serializers.ValidationError('Invalid password.')
        else:
            raise serializers.ValidationError('Manager does not exist.')

class ManagerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError('Incorrect old password.')
        return value

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'phone_number']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance
