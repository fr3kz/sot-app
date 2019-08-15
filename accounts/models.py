from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40,blank=True, null=True) 
    thumbnail = models.ImageField(upload_to="accounts")
    gold = models.IntegerField(default=0)
    solus = models.IntegerField(default=0)
    alliance = models.IntegerField(default=0)
    reputation = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Friendship(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    friends = models.ManyToManyField(User)

    def __str__(self):
        return self.profile.name          