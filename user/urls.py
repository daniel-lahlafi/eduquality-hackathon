from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('profile', views.UserProfileView.as_view()),
    path('sign-up', views.signup)
]