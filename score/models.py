from django.db import models
from django.core.validators import  MinValueValidator
from django.db import models
from django.core.validators import  MinValueValidator
from django.forms import ValidationError
from course.models import Enrolled

class Score(models.Model):
    enrolled    = models.ForeignKey(Enrolled, on_delete=models.CASCADE, related_name="scores")
    
    value       = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0)])
    name        = models.CharField(max_length=100, default="Final Score")
    comments    = models.TextField(null=True, blank=True)
    
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.value} ({self.enrolled.student.user.username})"

    def clean(self):
        super().clean()
        if self.value > 10:
            raise ValidationError("Value must be minor than 10")
        if self.value < 0:
            raise ValidationError("Value must be grater than 0")
