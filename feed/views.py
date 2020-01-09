from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.contrib.auth import get_user_model


from .models import UserFeed, FeedItem
from friends.models import Friendship
from user.models import UserProfile

from . import forms

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
            friends_username = [x.friend.username for x in Friendship.objects.filter(creator=self.request.user)]
            friends = Friendship.objects.filter(creator=self.request.user)
            friends_details = []
            for friend in friends:
                friends_details.append({
                    "username": friend.friend,
                    "image": get_object_or_404(UserProfile, user=friend.friend).image
                })

            context = {
                "username": self.request.user.username,
                "feed_items": FeedItem.objects.filter(feeds__user=self.request.user),
                "feed_item_form": forms.FeedItemForm(),
                "friends": friends_details,
            }
            
            return context

    def post(self, request):
        form = forms.FeedItemForm(request.POST)

        f = Friendship.objects.filter(
                friend = request.user
            )
        target_users = [x.creator for x in f]
        target_users.append(request.user)

        if form.is_valid():
            feed_item = FeedItem(author=request.user, description=form.cleaned_data['description'], pub_date=timezone.now())
            feed_item.save()

            for user in target_users:
                feed = UserFeed.objects.get(user=user)
                feed_item.feeds.add(feed)

        return HttpResponseRedirect('/feed')