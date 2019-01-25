from django.shortcuts import render,redirect
from .models import (Queue,Category)
from accounts.models import Profile

from django.contrib import messages
# Create your views here.
'''
display all users of  particular queue
{% for lobby in lobby%}
 {% for profile in lobby.usrs.all %}
    {{ profile.name}}
 {% endfor %}
{% endfor%}

'''
def index(request):

    fort  = Queue.objects.filter(category__title='Fort szkieletow')[:1]
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
        #TODO add frontend
    queue = Queue.objects.get(id=queue_id)
    
    context = {
        'queue':queue
    }

    return render(request,'lobby/detail.html', context)      

def add_user(request,queue_id):
    queue = Queue.objects.get(id=id)
    user = request.user
    all_users = queue.usrs.all
    #check if user is in this lobby
    if user in all_users:
        messages.error(request,'Juz tutaj jestes')
        return redirect('dashboard'+ queue_id)
    else:    
        queue.usrs.add(user)
        return redirect('dashboard'+ queue_id)


def remove_user(request,queue_id,user_id):
    queue = Queue.objects.get(id=id)
    user = User.objects.get(id=user_id)
    queue.usrs.remove(user)
    return redirect('dashboard'+ queue_id)
