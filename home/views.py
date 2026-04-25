from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from course.repository import ClassSectionRepository, EnrollRepository
from home.user_repositry import UserRepository
from student.repository import StudentRepository
from teacher.repository import TeacherRepository

def index (request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        user = request.user 
        if user.is_authenticated:
            return redirect("dashboard")
        return render(request, "index.html")

    return render(request, "error/404.html")

def login_user(request: HttpRequest)-> HttpResponse:
    
    if request.method == "GET":
        user = request.user 
        if user.is_authenticated:
            return redirect("home")
        return render(request, "auth_login.html")

    if request.method == "POST":
       username = request.POST.get("username", None)
       password = request.POST.get("password", None)
       ## for the next time just use autenticate this logic ist not reciclable 
       if password is None or username is None or username == "" or password == "":
            messages.error(request, "The password and username are required")
            return redirect("login_user")
        
       user = UserRepository.get_user_by_username(str(username))
       
       if user is None:
            messages.error(request, f"User {user} doesn't exist")
            return redirect("login_user")
       
       if not UserRepository.validate_password(user, str(password)):
            messages.error(request, "Incorrect password")
            return redirect("login_user")
       ## ---------------------------------------------
       login(request, user)
       
       return redirect("login_user")
    
    return render(request, "error/404.html")


def dashboard (request:  HttpRequest)-> HttpResponse:
    if request.method == "GET":
        context = {}
        user = request.user
        student = StudentRepository.is_student_by_id(user.id) 
        teacher = TeacherRepository.is_teacher_by_id(user.id)

        if student is not None:
            context["student"] = True
            enrolls_cntx = {}
            enrolls = EnrollRepository.get_enrollments_by_student_id(student.pk)
            for en in enrolls:
                enrolls_cntx[f"f{en.pk}"] = {
                    "name"          : en.class_section.course.name,
                    "description"   : en.class_section.course.description,
                    "sections"      : f"{en.class_section.teacher.id}-{en.class_section.course.id}",
                    "section_id"    : en.class_section.pk
                }
            context["enrolls"] = enrolls
        if teacher is not None:
             context["teacher"] = True
             secctions = {}
             class_section = ClassSectionRepository.get_class_sections_by_teacher_id(teacher.pk)
             if class_section is not  None:
                 for cs in class_section:
                     secctions[f"{cs.pk}"] = {
                        "name": cs.course.name,
                        "description": cs.course.description,
                        "sections": f"{cs.teacher.id}-{cs.course.id}",
                        "section_id"    : cs.pk
                     }
             
             context["sections"]= secctions

        return render(request, "dashboard.html", context=context)

    return render(request, "error/404.html")

def custom_404(request, exception):
    return render(request, "error/404.html", status=404)

