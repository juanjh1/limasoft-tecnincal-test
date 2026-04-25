from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Course, ClassSection, Enrolled
from student.models import Student
from teacher.models import Teacher

class CourseSecurityTests(TestCase):
    def setUp(self):
        self.teacher_user = User.objects.create_user(username='profe1', password='pass123')
        self.teacher = Teacher.objects.create(user=self.teacher_user)
        
        self.student_user = User.objects.create_user(username='alumno1', password='pass123')
        self.student = Student.objects.create(user=self.student_user, birth_day='2000-01-01')
        
        self.course = Course.objects.create(name='Matemáticas', max_capacity=1, code='MAT101')
        self.section = ClassSection.objects.create(course=self.course, teacher=self.teacher)

    def test_student_cannot_see_unrolled_scores(self):
        """Un alumno no debe poder ver notas de una sección donde no está inscrito"""
        self.client.login(username='alumno1', password='pass123')
        response = self.client.get(f'/score/scoreboard/{self.section.id}')
        self.assertEqual(response.status_code, 403)

    def test_teacher_cannot_see_others_sections(self):
        """Un profesor no debe poder ver notas de secciones que no le pertenecen"""
        user2 = User.objects.create_user(username='profe2', password='pass123')
        Teacher.objects.create(user=user2)
        
        self.client.login(username='profe2', password='pass123')
        response = self.client.get(f'/score/scoreboard/{self.section.id}')
        self.assertEqual(response.status_code, 403)

    def test_course_max_capacity_enforced(self):
        """El sistema no debe permitir exceder la capacidad máxima del curso"""
        Enrolled.objects.create(student=self.student, class_section=self.section)
        user2 = User.objects.create_user(username='alumno2', password='pass123')
        student2 = Student.objects.create(user=user2, birth_day='2000-01-01')
        with self.assertRaises(ValidationError):
            Enrolled.objects.create(student=student2, class_section=self.section)
