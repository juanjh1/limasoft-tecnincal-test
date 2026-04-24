from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from student.models import Student
from teacher.models import Teacher
# Create your models here.


class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT    = "DF", "DRAFT"
        ACTIVE   = "AC", "ACTIVE"
        INACTIVE = "IN", "INACTIVE"

    name         = models.CharField(max_length=60, validators=[MinLengthValidator(2)])
    max_capacity = models.IntegerField(validators=[MinValueValidator(1)])
    description  = models.CharField(null=True, blank=True, max_length=255)
    code         = models.CharField(max_length=30, validators=[MinLengthValidator(5)], unique=True)
    state        = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

class ClasssSection(models.Model):
    course_id  = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="couser_section")
    teacher_id = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="teacher_section")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course_id', 'teacher_id'], 
                name='unique_course_teacher'
            )
        ]

class Enrolled(models.Model): 
    student_id       = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="section_studen_enrolled")
    class_section_id = models.OneToOneField(ClasssSection, on_delete=models.CASCADE, related_name="class_section_enrolled")
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student_id', 'class_section_id'], 
                name='enroll_class_section'
            )
        ]

