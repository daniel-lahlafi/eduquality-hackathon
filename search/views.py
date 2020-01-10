from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views import generic

from user.models import UserProfile


def searchView(request, query):
    if request.user.is_authenticated:
        users = get_user_model().objects.filter(username=query)
        user_profiles = []
        for user in users:
            user_profiles.append({
                "username": user.username,
                "image": get_object_or_404(UserProfile, user=user).image,
            })

        

        context = {
            "user_profiles": user_profiles,
            "query": query
        }
        return render(request, 'search/search.html', context)