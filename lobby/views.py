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

    fort  = Queue.objects.filter(category__title='Fort szkieletow')
    atena = Queue.objects.filter(category__title='Atena')
    lobby = Queue.objects.filter(id=1)

    context = {
        'lobby':lobby,
        'fort':fort,
        'atena':atena,
    }
    return render(request, 'lobby/index.html',context)

def create(request):

    if request.method == 'POST':
        title    = request.POST['title']
        members  = request.POST['members']
        date     = request.POST['date']
        category = request.POST['category']

        categ = Category.objects.get(title=category) 

        if members > 4:
            messages.error(request,'maksymalna wartosc to 4')
            return redirect('create')
        else:
            queue = Queue(title=title,members=members,date=date,category=categ) 
            return redirect('dashboard')  
    else:
        return render(request, 'lobby/create.html')    

def dashboard(request, id):
    queue = Queue.objects.get(id=id)

    context = {
        'queue':queue
    }

    return render(request,'lobby/dashboard.html', context)       

#TODO add user 

def add_user(request,queue_id,user_id):
    pass    