from django.db import models
from django.contrib.auth import get_user_model

from feed.models import UserFeed

class ClassRoom(models.Model):
    name=models.TextField(unique=True)
    teacher=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    feed=models.ForeignKey(UserFeed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    class_room=models.ManyToManyField(ClassRoom, blank=True)

    def __str__(self):
        return self.user.username
    