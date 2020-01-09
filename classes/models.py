from django.db import models
from django.contrib.auth import get_user_model

from feed.models import UserFeed

class ClassRoom(models.Model):
    name=models.CharField(unique=True)
    teacher=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    feed=models.ForeignKey(UserFeed, on_delete=models.CASCADE)

class Student(models.Model):
    user=models.OneToOneField(get_user_model())
    class_room=models.ManyToManyField(Class)
