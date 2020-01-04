from django.db import models
from django.contrib.auth import get_user_model

class Friendship(models.Model):
    creator = models.ForeignKey(get_user_model(), related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(get_user_model(), related_name="friend_set", on_delete=models.CASCADE)

    def __str__(self):
        return (self.creator.username + " -> " +self.friend.username)
    