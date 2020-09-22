from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    email = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    #image = serializers.URLField(max_length=200)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)