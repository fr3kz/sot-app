from django.shortcuts import render,redirect
from .models import (Queue,Category,Query)
from accounts.models import Profile

from django.contrib import messages
# Create your views here.

def index(request):

    fort  = Queue.objects.order_by('-id')[:1]
    #atena = Queue.objects.get(category__title='Atena')
    # gold  = Queue.objects.get(category__title='Gold')
   #  lobby = Queue.objects.filter(id=1)
  
    context = {
     #   'lobby':lobby,
        'fort':fort,
     #   'atena':atena,
      #  'gold':gold,
    }
    return render(request, 'lobby/index.html',context)

def create(request):

    if request.method == 'POST':
        title    = request.POST['title']
        members  = request.POST['members']
        date     = request.POST['date']
        category = request.POST['category']

        categ = Category.objects.get(id=category) 
        queue = Queue(title=title,members=members,date=date,category=categ) 
        queue.save()
        return redirect('dashboard')  
    else:
        return render(request, 'lobby/create.html')    

def detail(request, queue_id):
    queue = Queue.objects.get(id=queue_id)
    
    context = {
        'queue':queue
    }

    return render(request,'lobby/detail.html', context) 

def dashboard(request, queue_id):

    queue = Queue.objects.get(id=queue_id)
    queries = Query.objects.filter(queue=queue)
    
    #TODO display all users in particular lobby
    #FIXME display special message if there s no query

    context = {
        'queue':queue,
        'queries': queries,
    }

    return render(request,'lobby/dashboard.html', context)     

def users_dashboard(request):
    user = request.user
    
    users_queue = Queue.objects.filter(usrs=user.profile)
    context = {
        'queue':users_queue
    }

    return render(request,'lobby/userdash.html', context)  

def add_user(request,queue_id,profile_id):
        queue = Queue.objects.get(id=queue_id)
        profile = Profile.objects.get(id=profile_id)
        queue.usrs.add(profile)
        query = Query.objects.get(queue=queue,profile=profile).delete()
        return redirect('dashboard', queue_id)

