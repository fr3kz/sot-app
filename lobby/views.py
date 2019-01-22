from django.shortcuts import render
from .models import Queue
from accounts.models import Profile
# Create your views here.
# TODO index,create,detail lobby function
def index(request):
    lobby = Queue.objects.filter(id=1)
    print(lobby)
    context = {
        'lobby':lobby,
    }
    return render(request, 'lobby/index.html',context)