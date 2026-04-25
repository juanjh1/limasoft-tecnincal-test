from django.core.exceptions import ObjectDoesNotExist
from course.models import ClasssSection, Course, Enrolled
from django.db.models import  QuerySet

class ClassSectionRepository:
    def __init__ (self) -> None:
        pass

    @staticmethod
    def get_class_sections_by_teacher_id(teacher_id: int) -> QuerySet[ClasssSection]:
        return ClasssSection.objects.filter(teacher_id=teacher_id)
    
    @staticmethod
    def get_class_sections_and_course_by_teacher_id(teacher_id: int) -> QuerySet[ClasssSection]:
        return ClasssSection.objects.filter(teacher_id=teacher_id).select_related('course')



class CourseRepository:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_course_by_id(id) -> Course | None:
        try: 
            return Course.objects.get(course_id=id)
        except ObjectDoesNotExist:
            return None


class EnrollRepository:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_enrrollment_by_student_id(id: int) -> QuerySet[Enrolled]:
        return Enrolled.objects.filter(student_id=id).select_related('class_section', 'class_section__course')
