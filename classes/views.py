from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404, reverse
from django.contrib.auth import get_user_model

from feed.models import UserFeed
from .models import ClassRoom, Student

def classView(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)
        student = get_object_or_404(Student, user=request.user)
        classes = student.class_room
        joined = None
        if classes.count() > 0:
            joined = classes.count()

        return render(request, 'classes/classRoom.html', {
            "name": class_room.name,
            "teacher": class_room.teacher,
            "feed": get_object_or_404(UserFeed, user=request.user),
            "joined": joined
        })
    else:
        return redirect('login')

def join_class(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)
        student = get_object_or_404(Student, user=request.user)
        student.class_room.add(class_room)

        return redirect('/classes/class/'+class_name)
    else:
        return redirect('login')

def leave_class(request, class_name):
    if request.user.is_authenticated:
        class_room = get_object_or_404(ClassRoom, name=class_name)
        student = get_object_or_404(Student, user=request.user)
        student.class_room.remove(class_room)

        return redirect('/classes/class/'+class_name)
    else:
        return redirect('login')

def create_class(request, class_name):
    if request.user.is_authenticated:
        ClassRoom(
            name=class_name,
            teacher=request.user,
            feed=get_object_or_404(UserFeed, user=request.user)
        ).save()
        return redirect(request, '/classes/class/'+class_name)
    else:
        return redirect('login')