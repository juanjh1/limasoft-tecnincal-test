from student.models import Student


class StudentRepository:
    def __init__(self) -> None:
        ...


    @staticmethod
    def is_student_by_id( id : int) -> Student | None:
        return Student.objects.get(user_id=5)
