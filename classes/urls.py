from django.urls import path

from . import views

app_name = 'classes'
urlpatterns = [
    path('class/<str:class_name>/', views.classView, name="class"),
    path('join/<str:class_name>/', views.join_class, name='join_class'),
    path('leave/<str:class_name>/', views.leave_class, name='leave_class'),
    path('create/<str:class_name>/', views.create_class, name='create_class')
]