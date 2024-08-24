from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .views_courses import index


def my_login(request):
    return render (request, 'courses/login.html', {})

def user_login(request):
    username = request.POST["usernae"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('courses:index')
    else:
        context = {
            'error_message': 'Nombre de usuario y/o contrasena incorrecto.'
        }
        return render(request, 'courses/login.html', context)
    
def user_logout(request):
    logout(request)
    return redirect('courses:login')   
