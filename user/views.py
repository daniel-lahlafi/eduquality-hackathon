from .models import UserProfile
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


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



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            profile = UserProfile(user=user)
            profile.city = form.cleaned_data.get('city')
            profile.phone = form.cleaned_data.get('phone')
            profile.image = form.cleaned_data.get('image')
            profile.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/feed')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
        