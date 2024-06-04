from rest_framework import serializers
from .models import Search

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['key']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance