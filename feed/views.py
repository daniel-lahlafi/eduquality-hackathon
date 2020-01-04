from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import generic

from .models import UserFeed, FeedItem

class FeedView(generic.ListView):
    """ Users feed """
    template_name = 'feed/feed.html'
    context_object_name = 'context'

    def render_to_response(self, context):
        if self.request.user.is_authenticated:
            return super().render_to_response(context)
        else:
            return redirect('login')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            context = {
                "username": self.request.user.username,
                "feed_items": FeedItem.objects.filter(feeds__user=self.request.user)
            }
            
            return context
