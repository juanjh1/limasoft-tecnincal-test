from django.contrib.auth.views import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from student.repository import StudentRepository
from teacher.repository import TeacherRepository
from course.repository import ClassSectionRepository, EnrollRepository
# Create your views here.


@login_required
def show_scores(request: HttpRequest, id:int) -> HttpResponse:
    if request.method == "GET":
        cs_section = ClassSectionRepository.get_class_section_by_id(id)
        if cs_section is None:
            return render(request,"error/404.html")

        context = {}
        context["section"]  = cs_section
        user = request.user
        student = StudentRepository.is_student_by_id(user.id) 
        teacher = TeacherRepository.is_teacher_by_id(user.id)
        
        if teacher is not None:
            context["teacher"] = True
            return render(request, "score_board.html", context=context ) 
  


        if student is not None :
            context["student"] = True
            enrollment = EnrollRepository.get_enrollment_by_class_section_id_and_student_id(id, student.pk)
            
            if enrollment is None:
                return render(request,"error/404.html") # unautorized 
            scores = enrollment.scores.all()
            context["scores"]   = scores
           
            return render(request, "score_board.html",context=context )

   
    return render(request,"error/404.html")
