from .models import Teacher
from django.core.exceptions import ObjectDoesNotExist
class TeacherRepository:
    def __init__(self) -> None:
        ...

    @staticmethod
    def is_teacher_by_id( id : int) -> Teacher | None:
        try:
             return Teacher.objects.get(user_id=id)
        except ObjectDoesNotExist:
            return None


