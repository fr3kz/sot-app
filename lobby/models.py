from django.db import models
from accounts.models import Profile
# Create your models here.

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

    def __str__(self):
      return self.title  