from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import generic

from .models import UserFeed, FeedItem

class FeedView(generic.ListView):
    """ Users feed """
    template_name = 'feed/feed.html'
    context_object_name = 'feed_list'

    def render_to_response(self, context):
        if self.request.user.is_authenticated:
            return super().render_to_response(context)
        else:
            return redirect('login')

    def get_queryset(self):
        request = self.request
        print(request.user)
        if request.user.is_authenticated:
            """Return the last five published questions."""
                        
            return FeedItem.objects.filter(
                feeds__user=request.user
            )
