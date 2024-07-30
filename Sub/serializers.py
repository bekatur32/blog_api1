from rest_framework import serializers
from .models import  Subscribed
from users.serializers import AuthorSerializer

class SubscribedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribed
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        subscribed = Subscribed(
            email=validated_data['email'],
            username=validated_data['username']
        )
        subscribed.set_password(validated_data['password'])
        subscribed.save()
        return subscribed
