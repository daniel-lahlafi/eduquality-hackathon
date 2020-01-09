from django.db import models
from django.contrib.auth import get_user_model
from friends.models import Friendship


class UserFeed(models.Model):
    user = models.OneToOneField(get_user_model(), 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username

class FeedItem(models.Model):
    author = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
    )
    feeds = models.ManyToManyField(UserFeed)
    description = models.TextField('description')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Author: %s, Description: %s" % (self.author, self.description[:10] + "...")