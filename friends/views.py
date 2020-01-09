from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Friendship
from django.contrib.auth import get_user_model

def create_friendship(request, username):
    if request.user.is_authenticated:
        target_user = get_object_or_404(get_user_model(), username=username)
        Friendship.objects.create(creator=request.user, friend=target_user)
        return redirect(reverse("feed:feed"))
    else:
        return redirect('login')
        
def remove_friendship(request, username):
    if request.user.is_authenticated:
        target_user = get_object_or_404(get_user_model(), username=username)
        friendship = get_object_or_404(Friendship, creator=request.user, friend=target_user)
        friendship.delete()
        return redirect(reverse("feed:feed"))
    else:
        return redirect('login')