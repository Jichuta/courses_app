from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout



def login_page(request):
    return render (request, 'courses/login.html', {})

def user_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        user_name = request.session.get('username')
        user_role = request.session.get('user_role')
        if user_name is not None and user_role is not None:
            return redirect('courses:index')
    
    username = request.POST["username"]
    password = request.POST["password"]
    role = request.POST.get("role")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        # Save username and role in session
        request.session['username'] = username
        request.session['user_role'] = role

        return redirect('courses:index')
    else:
        context = {
            'error_message': 'Nombre de usuario y/o contrasena incorrecto.'
        }
        return render(request, 'courses/login.html', context)
    
def user_logout(request):
    logout(request)
    return redirect('courses:login_page')   
