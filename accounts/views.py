from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from accounts.models import Profile
from lobby.models import Queue

# Create your views here.
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
            thumbnail = request.FILES['thumbnail']
            #add image
            fs = FileSystemStorage('lobby/')
            fs.save(thumbnail.name,thumbnail)
            thumbnail_name = 'accounts/' + thumbnail_name              
            
            #check if username and email is taken
            user = User.objects.get(username=username)
            if user is not None:
                    usr = User(username=username,password=password)
                    profile = Profile(name=name, thumbnail=thumbnail_name)
                    return redirect('index') 
            else:
                    messages.error(request,'Zajety username')
                    return redirect('login')     
        
    return render(request,'accounts/register.html')    