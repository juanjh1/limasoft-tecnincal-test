from django.core.exceptions import ObjectDoesNotExist
from course.models import ClasssSection, Course
from django.db.models import  QuerySet

class ClassSectionRepository:

    def __init__ (self) -> None:
        pass

    @staticmethod
    def get_class_sections_by_teacher_id(teacher_id: int) -> QuerySet[ClasssSection]:
        
        ClasssSection.objects.filter(teacher_id=teacher_id)


class CourseRepository:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_course_by_id(id) -> Course | None:
        try: 
            return Course.objects.get(course_id=id)
        except ObjectDoesNotExist:
            return None
