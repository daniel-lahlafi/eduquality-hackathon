from django.urls import path

from . import views

app_name = 'friends'
urlpatterns = [
    path('create/<str:username>/', views.create_friendship),
    path('remove/<str:username>/', views.remove_friendship)
]