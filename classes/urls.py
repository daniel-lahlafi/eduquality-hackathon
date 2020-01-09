from django.urls import path

from . import views

app_name = 'classes'
urlpatterns = [
    path('<str:class_name>', views.FeedView.as_view(), name="feed"),
    path('join/<str:class_name>')
    path('leave/<str:class_name')
    path('create/')

]