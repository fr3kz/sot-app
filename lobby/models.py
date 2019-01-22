from django.db import models
from accounts.models import Profile
# Create your models here.
class Queue(models.Model):
    title = models.CharField(max_length=50)
    members = models.IntegerField()
    date = models.DateTimeField()
    usrs = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title  

