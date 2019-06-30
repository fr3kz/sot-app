from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect,get_object_or_404
from .models import (Queue,Category,Query,Invitation,UserInvite,Notification)
from accounts.models import (Profile,Friendship)
from django.contrib import messages
from django.contrib.auth.models import User
from . import messages as mes
from .serializers import (CategorySerializer,QueueSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def index(request):
    n1queues  = Queue.objects.all()[:1]
    n2queues  = Queue.objects.all()[1:2]
    n3queues  = Queue.objects.all()[2:3]

    flobby   = Queue.objects.filter(category__title="Fort")[:3]
    alobby   = Queue.objects.filter(category__title="Atena")[:3]

    profiles = Profile.objects.order_by('-reputation')
    
    if request.user.is_authenticated:

        notification = Notification.objects.filter(user=request.user)
    else:
        notification = ""
        
    context  = {
        'n1fort':n1queues,
        'n2fort':n2queues,
        'n3fort':n3queues,
        'flobby':flobby,
        'alobby':alobby,
        'profiles':profiles,
        'notifications':notification
    }

    return render(request, 'lobby/index.html',context)

def create(request):

    if request.method == 'POST':
        title    = request.POST['title']
        members  = request.POST['members']
        date     = request.POST['date']
        category = request.POST['category']
        
        user = request.user
        profile = user.profile

        if user is None:
            messages.error(request,"nie jestes zalogowany")

            return redirect('create', queue.id)

        categ = Category.objects.get(id=category) 

        queue = Queue(title=title,members=members,date=date,category=categ,author=user)
        queue.save()

        queue.usrs.add(profile)

        return redirect('dashboard', queue.id)  

    else:
        
        categories = Category.objects.all()

        return render(request, 'lobby/create.html',{'categories':categories})    

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
        profile = Profile.objects.get(id=profile_id)
        
        queue = Queue.objects.get(id=queue_id)
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
    user = request.user
    profile = user.profile

    #invitations
    user_invites = Invitation.objects.filter(invited=profile)

    if request.method == 'POST':

        username = request.POST['username']

        if username:
            profile.username = username

        #thumbnail
        if request.FILES:
            thumbnail  = request.FILES['image']

            fs = FileSystemStorage('media/accounts')
            fs.save(thumbnail.name,thumbnail) 
            
            thumbnail_path = 'accounts/' + thumbnail.name

            profile.thumbnail = thumbnail_path

        profile.save()

        return redirect('profile')

    context = {
        'profile':profile,
        'invitations':user_invites,

    }

    return render(request,"lobby/profile.html",context)

def profile_detail(request,profile_id):
    
    profile = Profile.objects.get(id=profile_id)
    usr     = request.user

    context = {
        'profile': profile,
        'user': profile.user,
        'prof': usr.profile
    }

    return render(request,'lobby/profiledetail.html',context)

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

    #CREATE notification that user achieve +1 rep
    ausr = queue.author
    mes = mes.rep_plus(ausr)
    n = Notification(user=user,message=mes)
    n.save()

    return redirect('rate',queue_id)

def rep_downvote(request,user_id,queue_id):
    #user to -1 a rep
    user = User.objects.get(id=user_id)

    profile = user.profile
    profile.reputation = profile.reputation - 1
    profile.save()

    queue = Queue.objects.get(id=queue_id)
    queue.usrs.remove(profile)
    ausr = queue.author

    mes1 = mes.rep_down(ausr)
    n = Notification(user=user,message=mes1)
    n.save()

    return redirect('rate',queue_id)

def send_invite(request,invitator_id,invited_id):
    #send  invitationm to friend

    invitator        = User.objects.get(id=invitator_id)
    invitator_usr    = invitator.profile
    inv_id           = invitator_usr.id

    invited   = Profile.objects.get(id=invited_id)

    #check if user invite hisself 
    if invitator_usr.id == invited.id:
        
        messages.error(request,"Nie mozesz zaprosić samego siebie.")

        return redirect('profiledetail',invited_id)

    if Invitation(invited=invited).exists():

        messages.error(request, "Juz zaprosiłes tego gracza")

        return redirect('profile',invited_id)    

    invitation = Invitation(invited=invited)
    invitation.save()
    invitation.invitator.add(invitator)
    invitation.save()

    #send notification to invited  profile
    message = mes.send_invite_to_friends(invited)

    notification = Notification(user=invited.user,message=message)
    notification.save()

    return redirect('profile')

def accept_invite(request,invitator_id,invited_id):
    #accept request to add to friendship

    invitator         = User.objects.get(id=invitator_id)
    invitator_profile = invitator.profile

    invited           = Profile.objects.get(id=invited_id)

    invite            = Invitation.objects.get(invitator=invitator,invited=invited)   

    #ccheck if user has any firendship
    if Friendship.objects.filter(profile=invited).exists():

        #add to existing
        fren = Friendship.objects.get(profile=invited)
        fren.friends.add(invitator)
        fren.save()

    else:
        f = Friendship(profile=invited)
        f.save()
        f.friends.add(invitator)
        f.save()

    invite.delete()

    #add notification for user who sent inivte
    message = mes.accept_invite_to_friends(invitator_usr)

    notification = Notification(user=invitator,message=message)
    notification.save()

    return redirect('profile')

def reject_invite(request,invitator_id,invited_id):
   
    invitator     = User.objects.get(id=invitator_id)
    invitator_profile = invitator.profile

    invited       = Profile.objects.get(id=invited_id)

    invite        = Invitation.objects.get(invitator=invitator,invited=invited)   
    invite.delete()

    #add notification for user who sent inivte
    message = mes.reject_invite_to_friends(invitator_usr)

    notification = Notification(user=invitator,message=message)
    notification.save()

    return redirect('profile')

def delete_friend(request,friend_id):
    
    usr = request.user
    profile = usr.profile

    fs = Friendship.objects.get(profile=profile)

    for friend in fs.friends.all():

        if friend.id == friend_id:
            fs.friends.remove(friend)        

    return redirect('profile')

def show_options(request,queue_id):

    queue = Queue.objects.get(id=queue_id)
    
    user = request.user
    profile = user.profile

    friendship = Friendship.objects.get(profile=profile)

    context = {
        'queue':queue,
        'friendship':friendship
    }

    return render(request, "lobby/options.html",context)

def add_userinvite(request,queue_id,profile_id):

    queue = Queue.objects.get(id=queue_id)

    profile = Profile.objects.get(id=profile_id)

    #add usee invitation
    userinvite = UserInvite()
    userinvite.save()

    userinvite.queue = queue
    userinvite.save()

    userinvite.user = profile
    userinvite.save()

    #TODO add positive messages
    return redirect('profile')

def show_userinvites(request,profile_id):

    profile = Profile.objects.get(id=profile_id)

    userinvi = UserInvite.objects.filter(user=profile)

    context = {
        'invitation':userinvi,
    }

    return render(request, "lobby/userinvitations.html",context)

def accept_userinvitation(request,ivitation_id):

    user_invitation = UserInvite.objects.get(id=ivitation_id)

    queue = user_invitation.queue
    profile  = user_invitation.user

    queue.usrs.add(profile)

    user_invitation.delete()

    return redirect('index')

def delete_userinvitation(request,ivitation_id):

    user_invitation = UserInvite.objects.get(id=ivitation_id)
    user_invitation.delte()

    return redirect('index')

def delete_notification(request,notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()

    return redirect('index')

def categories_list(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
        
    }

    return render(request, "lobby/categories.html", context)

def category_detail(request,category_id):
    category = Category.objects.get(id=category_id)

    queues = category.queue.all()

    context = {
        'category': category,
        'queues': queues
    }

    return render(request, "lobby/categorydetail.html", context)

####### api #####
class CategoriesList(APIView):

    def get(self,request,format=None):

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

    def post(self,request,format=None):

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class QueuesList(APIView):

    def get(self,request,format=None):

        category = Queue.objects.all()
        serializer = QueueSerializer(category, many=True)

        return Response(serializer.data)


    def post(self,request):

        serializer = QueueSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#auth
 