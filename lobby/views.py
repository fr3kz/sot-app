from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect,get_object_or_404
from .models import (Queue,Category,Query)
from accounts.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def index(request):
    #FOR PRODUCTION ONLY
    n1queues  = Queue.objects.order_by('-id')[:1]
    n2queues  = Queue.objects.order_by('-id')[:1]
    n3queues  = Queue.objects.order_by('-id')[:1]
    #n1_id = n1queues.id + 1
    #n2queues  = Queue.objects.filter(id=n1_id)
    #n2_id = n2queues.id + 1
    #n3queues  = Queue.objects.filter(id=n2_id)
    flobby   = Queue.objects.filter(category__title="Fort")
    alobby   = Queue.objects.filter(category__title="Atena")
    profiles = Profile.objects.order_by('-reputation')

    context  = {
        'n1fort':n1queues,
        'n2fort':n2queues,
        'n3fort':n3queues,
        'flobby':flobby,
        'alobby':alobby,
        'profiles':profiles
    }
    return render(request, 'lobby/index.html',context)

def create(request):
    if request.method == 'POST':
        title    = request.POST['title']
        members  = request.POST['members']
        date     = request.POST['date']
        category = request.POST['category']
        
        user = request.user

        if user is None:
            messages.error(request,"nie jestes zalogowany")
            return redirect('create', queue.id)

        profile = user.profile
        categ = Category.objects.get(id=category) 
        queue = Queue(title=title,members=members,date=date,category=categ,author=user)
        queue.save()
        queue.usrs.add(profile)
        return redirect('dashboard', queue.id)  
    else:
        return render(request, 'lobby/create.html')    

def detail(request, queue_id):
    queue = Queue.objects.get(id=queue_id)
    
    context = {
        'queue':queue
    }

    return render(request,'lobby/detail.html', context) 

def dashboard(request, queue_id):
    user = request.user
    user_id = user.id
    queue = Queue.objects.get(id=queue_id)
    author_id = queue.author.id
    if user_id == author_id:
        queue = Queue.objects.get(id=queue_id)
        queries = Query.objects.filter(queue=queue)

        context = {
            'queue':queue,
            'queries': queries,
        }

        return render(request,'lobby/dashboard.html', context)
    else:
        messages.error(request,"nie masz dostępu")
        return redirect('index')

def update_dash(request,queue_id):
    title    = request.POST['title']
    members  = request.POST['members']
    date     = request.POST['date']
    cateogry = request.POST['category']

    queue = Queue.objects.get(id=queue_id)
    if members:
        queue.members = members
    if title:
        queue.title = title
    if date:
        queue.date = date
    if cateogry:
        cat = Category.objects.get(id=cateogry)
        queue.category = cat
    queue.save()
    return redirect('dashboard', queue_id)         

def delete_dash(request,queue_id):
    user = request.user
    queue = Queue.objects.get(id=queue_id)
    author_id = queue.author.id
    if user.id == author_id:
        queue.delete()
        return redirect('index')
    else:
        messages.error(request,"nie masz dostępu")
        return redirect('index')   

def users_dashboard(request):
    user = request.user
    participate_queue = Queue.objects.filter(usrs=user.profile)
    authors_queue     = Queue.objects.filter(author=user) 

    context = {
        'pqueue':participate_queue,
        'aqueue': authors_queue

    }

    return render(request,'lobby/userdash.html', context)  

def add_user(request,queue_id,profile_id):
        queue = Queue.objects.get(id=queue_id)
        profile = Profile.objects.get(id=profile_id)
        queue.usrs.add(profile)
        query = Query.objects.get(queue=queue,profile=profile).delete()
        return redirect('dashboard', queue_id)

def add_query(request,queue_id):
    
    user = request.user
    profile = user.profile
    queue = Queue.objects.get(id=queue_id)
    
    #check if user already attend or quered
    if Query.objects.filter(queue=queue,profile=profile).exists():
        messages.error(request,'jestes juz tutaj quered')
        return redirect('detail', queue.id)
    elif Queue.objects.filter(usrs=profile,id=queue_id).exists():
        messages.error(request,'jestes juz tutaj ')
        return redirect('detail', queue.id) 
    else:
        #add query
        q = Query(profile=profile,queue=queue)
        q.save()
        return redirect('detail', queue.id)

def profile(request):
    #TODO add frontend
    user = request.user
    profile = user.profile

    if request.method == 'POST':

        name = request.POST['name']
        img  = request.FILES['image']

        if name:
            profile.name == name

        #thumbnail
        if thumbnail:
            fs = FileSystemStorage('media/accounts/')
            fs.save(thumbnail.name,thumbnail) 
            
            thumbnail_path = 'accounts/' + thumbnail.name

            profile.thumbnail == thumbnail_path

        profile.save()       

        return redirect('profile',profile.id)

    context = {
        'profile':profile
    }

    return render(request,"lobby/profile.html",)

def rate(request,queue_id):
    user    = request.user
    profile = user.profile
    queue   = Queue.objects.get(id=queue_id)

    queue_users = queue.usrs.all

    context = {
        'members':queue_users,
        'queue_id':queue_id,
        'user_id': user.id
    }

    return render(request,"lobby/rate.html",context)

def rep_plus(request,user_id,queue_id):
    #user to +1 a rep ajax funtion
    queue = Queue.objects.get(id=queue_id)
    user = User.objects.get(id=user_id)
    profile = user.profile
    profile.reputation = profile.reputation + 1
    profile.save()
    queue.usrs.remove(profile)

    return redirect('rate',queue_id)

def rep_downvote(request,user_id,queue_id):
    #user to -1 a rep
    queue = Queue.objects.get(id=queue_id)
    user = User.objects.get(id=user_id)
    profile = user.profile
    profile.reputation = profile.reputation - 1
    profile.save()
    queue.usrs.remove(profile)

    return redirect('rate',queue_id)

def profile_detail(request,profile_id):
    profile = Profile.objects.get(id=profile_id)

    context = {
        'profile': profile
    }

    return render(request,'lobby/profiledetail.html',context)
