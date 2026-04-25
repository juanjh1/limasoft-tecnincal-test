from django.contrib.auth.views import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json
from student.repository import StudentRepository
from teacher.repository import TeacherRepository
from course.repository import ClassSectionRepository, EnrollRepository
from score.models import Score

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
            if cs_section.teacher_id != teacher.pk:
                return render(request, "error/403.html", status=403)
            
            context["teacher"] = True
            enrollments = cs_section.section_enrollments.all().select_related('student__user').prefetch_related('scores')
            
            # 1. Obtener nombres únicos de evaluaciones (Columnas)
            assessment_names = list(Score.objects.filter(enrolled__class_section=cs_section) \
                                          .values_list('name', flat=True) \
                                          .distinct() \
                                          .order_by('name'))
            context["assessment_names"] = assessment_names
            
            # 2. Construir la matriz de datos usando el Repositorio
            grade_matrix = []
            for enroll in enrollments:
                student_scores = []
                for name in assessment_names:
                    # Usamos el método del repositorio como pediste
                    score = EnrollRepository.get_score_for_enrollment_by_name(enroll, name)
                    student_scores.append({
                        'name': name,
                        'value': score.value if score else None
                    })
                
                grade_matrix.append({
                    'enroll': enroll,
                    'grades': student_scores
                })
            
            context["grade_matrix"] = grade_matrix
            return render(request, "score_board.html", context=context) 

        if student is not None:
            context["student"] = True
            enrollment = EnrollRepository.get_enrollment_by_class_section_id_and_student_id(id, student.pk)
            
            if enrollment is None:
                return render(request, "error/403.html", status=403)
            
            scores = enrollment.scores.all()
            context["scores"] = scores
            return render(request, "score_board.html", context=context)
    
    return render(request, "error/404.html")

@login_required
@require_POST
def add_score(request: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(request.body)
        enroll_id = data.get("enroll_id")
        score_name = data.get("name")
        value = data.get("value")
        comments = data.get("comments", "")

        if not enroll_id or not score_name or value is None:
            return JsonResponse({"status": "error", "message": "Incomplete data"}, status=400)

        teacher = TeacherRepository.is_teacher_by_id(request.user.id)
        enrollment = EnrollRepository.get_enrollment_by_id(enroll_id)

        if not teacher or not enrollment or enrollment.class_section.teacher_id != teacher.pk:
            return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

        score = Score.objects.create(
            enrolled=enrollment,
            name=score_name,
            value=value,
            comments=comments
        )

        return JsonResponse({"status": "success", "message": "Grade recorded successfully"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@login_required
@require_POST
def bulk_update_scores(request: HttpRequest) -> JsonResponse:
    try:
        data = json.loads(request.body)
        changes = data.get("changes", [])
        
        teacher = TeacherRepository.is_teacher_by_id(request.user.id)
        if not teacher:
            return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

        for item in changes:
            enroll_id = item.get("enroll_id")
            score_name = item.get("name")
            value = item.get("value")

            enrollment = EnrollRepository.get_enrollment_by_id(enroll_id)
            if enrollment and enrollment.class_section.teacher_id == teacher.pk:
                if value == "" or value is None:
                    continue
                
                Score.objects.update_or_create(
                    enrolled=enrollment,
                    name=score_name,
                    defaults={'value': value}
                )

        return JsonResponse({"status": "success", "message": "Grades updated successfully"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
