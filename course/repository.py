from django.core.exceptions import ObjectDoesNotExist
from course.models import ClassSection, Course, Enrolled
from score.models import Score
from django.db.models import QuerySet

class ClassSectionRepository:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_class_sections_by_teacher_id(teacher_id: int) -> QuerySet[ClassSection]:
        return ClassSection.objects.filter(teacher_id=teacher_id)
    
    @staticmethod
    def get_class_sections_with_course_by_teacher_id(teacher_id: int) -> QuerySet[ClassSection]:
        return ClassSection.objects.filter(teacher_id=teacher_id).select_related('course')
    @staticmethod
    def get_class_section_by_id(section_id: int) -> ClassSection | None:
        try:
            return ClassSection.objects.get(id=section_id)
        except ObjectDoesNotExist:
            return None

class CourseRepository:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_course_by_id(course_id: int) -> Course | None:
        try: 
            return Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            return None

class EnrollRepository:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_enrollments_by_student_id(student_id: int) -> QuerySet[Enrolled]:
        return Enrolled.objects.filter(student_id=student_id).select_related('class_section', 'class_section__course')
    
        return Enrolled.objects.filter(student_id=student_id).select_related(
            'class_section__course'
        ).prefetch_related('scores')

    @staticmethod
    def get_enrollment_by_id(enroll_id: int) -> Enrolled | None:
        try:
            return Enrolled.objects.get(id=enroll_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_enrollment_by_id_and_student_id(enroll_id: int, student_id: int) -> Enrolled | None:
        try:
            return Enrolled.objects.get(id=enroll_id, student_id=student_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_enrollment_by_class_section_id_and_student_id(cs_id: int, student_id: int) -> Enrolled | None:
        try:
            return Enrolled.objects.get(class_section=cs_id, student_id=student_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_score_for_enrollment_by_name(enrollment: Enrolled, name: str):
        return enrollment.scores.filter(name=name).first()
