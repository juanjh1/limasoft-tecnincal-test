from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from home.user_repositry import UserRepository
from student.repository import StudentRepository

def login_student (request: HttpRequest)-> HttpResponse:
    
    if request.method == "GET":
        return render(request, "student_login.html")

    if request.method == "POST":
       username = request.POST.get("username", None)
       password = request.POST.get("password", None)

       if password is None or username is None or username == "" or password == "":
            messages.error(request, "The password and username are required")
            return redirect("login-student")
        
       user = UserRepository.get_user_by_username(str(username))
       
       if user is None:
            messages.error(request, f"User {user} doesn't exist")
            return redirect("login-student")
       
       if not UserRepository.validate_password(user, str(password)):
            messages.error(request, "Incorrect password")
            return redirect("login-student")

       if StudentRepository.is_student_by_id(user.pk) is None:
            messages.error(request, f"User {user.username} is not student")
            return redirect("login-student")
       login(request, user)
       messages.success(request, f"Welcome {user.username}")
       return redirect("login-student")
    
    return render(request, "404.html")
