from rest_framework import serializers
from .models import (Queue,Category)
from accounts.models import Profile
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title')

    def create(self, validated_data):
        title = validated_data.pop('title')

        return Category.objects.create(title=title)


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
    class Meta:
        model = Queue
        fields = ('id','title','members',"date","category","author","usrs")

    def create(self,validated_data):
        title = validated_data.get('title')
        members = validated_data.get('members')
        date =  validated_data.get('date')

        category = validated_data.get('category')
        cat = Category.objects.get(title=category)

        #pass only id of the author
        author = validated_data.get('author')
        aut = User.objects.get(username=author)

        usrs = validated_data.get('usrs')

        queue = Queue(title=title,members=members,date=date,category=cat,author=aut)
        queue.save()

        for usr in usrs:
            queue.usrs.add(usr)
            queue.save()
            
        return queue         
