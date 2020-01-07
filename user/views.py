from django.shortcuts import render
from .models import UserProfile
from django.views import generic


class UserProfileView(generic.ListView):
    template_name = 'user/userProfile.html'
    context_object_name = 'context'

    def render_to_response(self, context):
        if self.request.user.is_authenticated:
            return super().render_to_response(context)
        else:
            return redirect('login')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            context = {
                "profile": UserProfile.objects.get(user=self.request.user)
            }
            return context
        