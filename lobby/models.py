from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
# Creatse your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Queue(models.Model):
    title = models.CharField(max_length=50)
    members = models.IntegerField()
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,blank=True,null=True)
    usrs = models.ManyToManyField(Profile)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
      return self.title  

    def pretty_date(self):
        return self.date.strftime('%Y-%m-%d %H:%M')

    class Meta:
        ordering = ['-id']      

class Query(models.Model):
    queue = models.OneToOneField(Queue, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return "Query"

class Invitation(models.Model):
    invitator = models.ManyToManyField(User)
    invited   = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "Invite"

class UserInvite(models.Model):
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, blank=True,null=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return "UserInvite"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    redirect = models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return 'Notification ' + self.user.username                