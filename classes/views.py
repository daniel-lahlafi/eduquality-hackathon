from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404, reverse
from django.contrib.auth import get_user_model

from feed.models import UserFeed
from .models import ClassRoom, Student

from . import forms

def classView(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)

        return render('classes/classRoom.html', {
            "name": class_room.name,
            "teacher": class_room.teacher,
            "feed": UserFeed.get(user=request.user),
            "joined": Student.objects.filter(user=request.user, name=class_name)
        })
    else:
        return redirect('login')

def join_class(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)
        student = Student(user=request.user)
        student.class_room.add(class_room)

        return render(reverse('classes:classroom'), class_room=class_name)
    else:
        return redirect('login')

def leave_class(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)
        student = get_object_or_404(user=request.user, class_room=class_room)
        student.remove()
    else:
        return redirect('login')

def create_class(request, class_name):
    if request.user.is_authenticated:
        ClassRoom(
            name=class_name,
            teacher=request.user
            feed=UserFeed.get(user=request.user)
        ).save()
    else:
        return redirect('login')