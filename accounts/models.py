from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=40) 
    thumbnail = models.ImageField(upload_to="accounts")
    gold = models.IntegerField()
    solus = models.IntegerField()
    alliance = models.IntegerField()
    reputation = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name      