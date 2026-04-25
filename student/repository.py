from .models import Student
from django.core.exceptions import ObjectDoesNotExist

class StudentRepository:
    def __init__(self) -> None:
        ...


    @staticmethod
    def is_student_by_id( id : int) -> Student | None:
        try:
            return Student.objects.get(user_id=id)
        except ObjectDoesNotExist:
            return None
