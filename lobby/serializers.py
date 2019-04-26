from rest_framework import serializers
from .models import (Queue,Category)
from accounts.models import Profile
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def updated(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')

class UsrsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = ('id','thumbnail','gold','solus','alliance','reputation','user')

class QueueSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    usrs     = UsrsSerializer(many=True)
    author   = UserSerializer(many=False)
    class Meta:
        model = Queue
        fields = ('id','title','members',"date","category","usrs","author","complete")
    