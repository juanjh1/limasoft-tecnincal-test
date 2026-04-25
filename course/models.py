from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from student.models import Student
from teacher.models import Teacher

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

    def __str__(self):
        return f"{self.name} ({self.code})"

class ClassSection(models.Model):
    course  = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="sections")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'teacher'], 
                name='unique_course_teacher'
            )
        ]
    
    def __str__(self):
        return f"{self.course.name} - {self.teacher.user.get_full_name()}"

class Enrolled(models.Model): 
    student       = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_enrollments")
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name="section_enrollments")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'class_section'], 
                name='enroll_class_section'
            )
        ]

    def save(self, *args, **kwargs):
        if not self.pk: 
            current_count = Enrolled.objects.filter(class_section=self.class_section).count()
            if current_count >= self.class_section.course.max_capacity:
                raise ValidationError("The course capacity is exceeded")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.user.username} - {self.class_section.course.name}"
