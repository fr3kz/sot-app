from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import (QueueSerializer,CategorySerializer,UserSerializer)

from .models import (Queue,Category,Query)
from django.contrib.auth.models import User
class IndexApi(viewsets.ModelViewSet):
    
    queryset = Queue.objects.all()

    serializer_class = QueueSerializer

class CategoryApi(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

class UserApi(viewsets.ModelViewSet):
    
    queryset = User.objects.all()

    serializer_class = UserSerializer  