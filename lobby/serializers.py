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
    category = serializers.PrimaryKeyRelatedField(many=False,queryset=Queue.category)
    usrs     = serializers.PrimaryKeyRelatedField(many=True,queryset=Queue.usrs)
    author   = serializers.PrimaryKeyRelatedField(many=False,queryset=Queue.author)
    class Meta:
        model = Queue
        fields = ('id','title','members',"date","category","usrs","author","complete")

    def save(self):
        title = self.validated_data['title']
        print(title)    

