from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('profile', views.UserProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', views.otherUserView, name='other_user'),
    path('sign-up', views.signup)
]