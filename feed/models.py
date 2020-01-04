from django.db import models
from django.contrib.auth import get_user_model

class UserFeed(models.Model):
    user = models.OneToOneField(get_user_model(), 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
    

class FeedItem(models.Model):
    feeds = models.ManyToManyField(UserFeed)
    author = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
    )
    description = models.TextField('description')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Author: %s, Description: %s" % (self.author, self.description[:10] + "...")
    
