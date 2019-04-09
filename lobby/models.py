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
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,blank=True,null=True, related_name='cat')
    usrs = models.ManyToManyField(Profile)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
      return self.title  

    def pretty_date(self):
        return self.date.strftime('%Y-%m-%d %H:%M')

class Query(models.Model):
    queue = models.OneToOneField(Queue, on_delete=models.DO_NOTHING)
    profile = models.OneToOneField(Profile,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Query"

class Invitation(models.Model):
    invitator = models.ManyToManyField(User)
    invited   = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Invite"            