from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from accounts.models import Profile
from lobby.models import Queue
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt import tokens
#auth via frontend
def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
                auth.login(request,user)
                return redirect('index')
        else:
                messages.error(request,"Zle dane")
                return redirect('login')   

     else:
        return render(request, 'accounts/login.html')


def register(request):

    if request.method == 'POST':
            name      = request.POST['name']
            username  = request.POST['username']
            password  = request.POST['password']
           # thumbnail = request.FILES['thumbnail']
            #add image
          #  fs = FileSystemStorage('lobby/')
          #  fs.save(thumbnail.name,thumbnail)
          #  thumbnail_name = 'accounts/' + thumbnail_name              
            
            #check if username and email is taken
            user = User.objects.get(username=username)
            if user is not None:
                    usr = User.objects.create_user(username=username,password=password)
                    profile = Profile(name=name,user=usr).save()
                    return redirect('index') 
            else:
                    messages.error(request,'Zajety username')
                    return redirect('login')     
        
    return render(request,'accounts/register.html')

def logout(request):

        auth.logout(request)
        return redirect('index')

#authenticate via rest api

class Login(APIView):
        def post(self,request,format=None):
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username,password=password)

                if user is not None:
                        token = RefreshToken.for_user(user)
                        print(token)
                        return Response({
                                'token':str(token.access_token),
                                'message':'zalogowano'
                                })
                else:
                        return Response({'message':'zle dane'})

class Register(APIView):
        def post(self,request,format=None):
                name = request.POST['name']
                username = request.POST['username']
                password = request.POST['password']
               # thumbnail = request.FILES['thumbnail']
                   
                user = User.objects.filter(username=username).exists()
                if user == False:
                    usr = User.objects.create_user(username=username,password=password)
                    profile = Profile(name=name,user=usr)

                    token = RefreshToken.for_user(usr)

                    return Response({ 
                        'message':'utworzono konto',
                        'token': str(token.access_token)
                        })
                else:
                    return Response({'message':'username jest zajety'})    